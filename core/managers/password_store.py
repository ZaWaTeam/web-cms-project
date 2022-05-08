import datetime
import logging
import os

import bcrypt
from peewee import Model, SqliteDatabase, AutoField, TextField, IntegerField, DateTimeField


class DBAlreadyExistsException(Exception):
    def __init__(self, db_name):
        self.db_name = db_name

    def __str__(self):
        return f"DBAlreadyExistsException: {self.db_name}. Try create(overwrite=True) to ignore this error"


class PasswordDB(object):
    def __init__(self, fp, iter_count=14):
        logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(asctime)s.%(msecs)03d - %(message)s',
                            datefmt='%H:%M:%S')
        self.fp = fp
        self.iter_count = iter_count
        self.db = None

    def create(self, overwrite=False):
        if overwrite:
            os.remove(self.fp)
        if os.path.exists(self.fp):
            raise DBAlreadyExistsException(self.fp)

        db = SqliteDatabase(self.fp)

        class BaseModel(Model):
            class Meta:
                database = db

        class PasswordStorage(BaseModel):
            id = AutoField()
            username = TextField()
            salted_password = TextField()
            salt = TextField()
            iter_count = IntegerField()
            timestamp = DateTimeField(default=datetime.datetime.now)

        db.connect()
        try:
            db.create_tables([PasswordStorage, ])
            logging.info(f"CONNECTED TO {db.database}")
            self.db = db
        except Exception as e:
            logging.error(f'{e.__repr__()}')

    def connect(self):
        db = SqliteDatabase(self.fp)
        db.connect()
        logging.info(f"CONNECTED TO {db.database}")

    def add(self, username, password):
        if self.db:
            class BaseModel(Model):
                class Meta:
                    database = self.db

            class PasswordStorage(BaseModel):
                id = AutoField()
                username = TextField()
                salted_password = TextField()
                salt = TextField()
                iter_count = IntegerField()
                timestamp = DateTimeField(default=datetime.datetime.now)

            salt = bcrypt.gensalt(rounds=self.iter_count)
            hashed_password = bcrypt.hashpw(password.encode('ascii'), salt)
            q = PasswordStorage.insert(username=username, salted_password=hashed_password, salt=salt,
                                       iter_count=self.iter_count)
            q.execute()
            logging.info("ADDED '%s' with password %s for %s iterations with salt: %s", username, hashed_password,
                         self.iter_count, salt)
            logging.debug(q)

    def insert(self, username, password):
        self.add(username, password)

    def remove(self, arg):
        class BaseModel(Model):
            class Meta:
                database = self.db

        class PasswordStorage(BaseModel):
            id = AutoField()
            username = TextField()
            salted_password = TextField()
            salt = TextField()
            iter_count = IntegerField()
            timestamp = DateTimeField(default=datetime.datetime.now)

        if isinstance(arg, int):
            u = PasswordStorage.get(PasswordStorage.id == arg).username
            PasswordStorage.delete_by_id(arg)
            logging.info('DELETED USER %s BY ID: %s', u, arg)
        elif isinstance(arg, str):
            i = PasswordStorage.get(PasswordStorage.username == arg).id
            PasswordStorage.get(PasswordStorage.username == arg).delete_instance()
            logging.info('DELETED USER WITH ID %s BY USERNAME: %s', i, arg)
        else:
            raise AttributeError('Got no username/id. Use: remove("username") or remove(12).')

    def check_password(self, arg, password):
        class BaseModel(Model):
            class Meta:
                database = self.db

        class PasswordStorage(BaseModel):
            id = AutoField()
            username = TextField()
            salted_password = TextField()
            salt = TextField()
            iter_count = IntegerField()
            timestamp = DateTimeField(default=datetime.datetime.now)

        if isinstance(arg, int):
            pwd = PasswordStorage.get(PasswordStorage.id == arg).salted_password.encode('ascii')
            u = PasswordStorage.get(PasswordStorage.id == arg).username
            result = bcrypt.checkpw(password.encode('ascii'), pwd)
            logging.info('CHECKED PASSWORD FOR USER \'%s\' WITH ID %s: %s', u, arg, 'VALID' if result else "INVALID")
            return result
        elif isinstance(arg, str):
            pwd = PasswordStorage.get(PasswordStorage.username == arg).salted_password.encode('ascii')
            u = PasswordStorage.get(PasswordStorage.username == arg).id
            result = bcrypt.checkpw(password.encode('ascii'), pwd)
            logging.info('CHECKED PASSWORD FOR USER \'%s\' PASSWORD WITH ID %s: %s', arg, u,
                         'VALID' if result else "INVALID")
            return result
        else:
            raise AttributeError('Got no username/id. Use: check_password("username", "pass") or remove(12, "pass").')

    def delete(self, arg):
        self.remove(arg)