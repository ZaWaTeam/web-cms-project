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


CpDb.create_tables([Configuration, Editables])
