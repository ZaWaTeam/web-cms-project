from core.configparse import config
from peewee import MySQLDatabase, SqliteDatabase

if config["DATABASE"]["Driver"] == "MySql":
    CpDb = MySQLDatabase(config["DATABASE"]["Name"],
                         host=config["DATABASE"]["Host"],
                         port=int(config["DATABASE"]["Port"]),
                         user=config["DATABASE"]["User"],
                         password=config["DATABASE"]["Password"])

elif config["DATABASE"]["Driver"] == "Sqlite":
    CpDb = SqliteDatabase(config["DATABASE"]["Path"])

else:
    # TODO: Create custom exception
    raise ValueError
