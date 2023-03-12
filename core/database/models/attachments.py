import peewee as pw
from typing import Optional
from core.database.connect import CpDb
from core.database.models.main import UserModel

class Attachment(pw.Model):
    id: int = pw.AutoField()
    name: str = pw.CharField()
    size: int = pw.IntegerField()
    type: str = pw.CharField()
    attachment: str = pw.TextField()
    author: Optional[UserModel] = pw.ForeignKeyField(UserModel, null=True)

    class Meta:
        database = CpDb

# Create base model
base_models = [Attachment]