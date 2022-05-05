from core.configparse import config
from peewee import MySQLDatabase

CpDb = MySQLDatabase(config["DATABASE"]["Name"], host=config["DATABASE"]["Host"], port=int(config["DATABASE"]
                                                                                           ["Port"]), user=config["DATABASE"]["User"], password=config["DATABASE"]["Password"])
