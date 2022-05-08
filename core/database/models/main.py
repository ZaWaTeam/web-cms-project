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


class UserModel(pw.Model):
    """
    WebCms User Model
    """
    id = pw.AutoField()
    username = pw.CharField(max_length=90)
    email = pw.CharField(max_length=90)
    password = pw.TextField()
    group = pw.ForeignKeyField(model=Groups, on_delete="CASCADE")

    class Meta:
        database = CpDb


class Permissions(pw.Model):
    """
    Permissions Model
    """
    id = pw.AutoField()
    permission = pw.CharField(max_length=200)
    group = pw.ForeignKeyField(Groups)

    class Meta:
        database = CpDb


CpDb.create_tables([Configuration, Editables, Groups, UserModel, Permissions])
