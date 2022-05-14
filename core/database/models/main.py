import peewee as pw
from core.database.connect import CpDb

# Configuration database


class Configuration(pw.Model):
    name = pw.CharField()
    value = pw.TextField()

    class Meta:
        database = CpDb


class Editables(pw.Model):
    name = pw.CharField()
    value = pw.TextField()
    index = pw.IntegerField()

    class Meta:
        database = CpDb


"""
Authorization scope
"""


class Groups(pw.Model):
    """
    Groups Model
    """
    id = pw.AutoField()
    name = pw.CharField(max_length=90)

    class Meta:
        database = CpDb

    def __repr__(self):
        return f"Groups(id={self.id}, name={self.name})"


class UserModel(pw.Model):
    """
    WebCms User Model
    """
    id = pw.AutoField()
    username = pw.CharField(max_length=90, unique=True)
    email = pw.CharField(max_length=90)
    password = pw.TextField()
    group = pw.ForeignKeyField(model=Groups, null=True, on_delete="CASCADE")

    class Meta:
        database = CpDb

    def __repr__(self):
        return f"UserModel(id={self.id}, " \
               f"username={self.username}, " \
               f"email={self.email}, " \
               f"password={self.password}, " \
               f"group={self.group})"


class Permissions(pw.Model):
    """
    Permissions Model
    """
    id = pw.AutoField()
    permission = pw.CharField(max_length=200)
    group = pw.ForeignKeyField(Groups, on_delete="CASCADE", null=True)
    user = pw.ForeignKeyField(UserModel, on_delete="CASCADE", null=True)

    class Meta:
        database = CpDb


class Sessions(pw.Model):
    """
    User login session.
    """
    id = pw.AutoField()
    user = pw.ForeignKeyField(UserModel, on_delete="CASCADE")
    device = pw.CharField(max_length=255)
    ip = pw.IPField()
    expires = pw.DateField()
    status = pw.CharField(max_length=10, default="active")
    token = pw.TextField()

    class Meta:
        database = CpDb


CpDb.create_tables([Configuration, Editables, Groups, UserModel, Sessions, Permissions])
