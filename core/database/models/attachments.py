import peewee as pw
from typing import Literal, Optional
from core.database.connect import CpDb
from core.database.models.main import UserModel

class Attachment(pw.Model):
    id: int = pw.AutoField()
    name: str = pw.CharField()
    size: int = pw.IntegerField()
    type: Literal['video', 'audio', 'picture', 'file'] = pw.CharField() # What type can be an attachment? ['video', 'audio', 'picture', 'file']
    attachment: str = pw.TextField()
    status: Literal["moderation", "cancled", "published"]
    author: Optional[UserModel] = pw.ForeignKeyField(UserModel, null=True)
    created_at: pw.DateTimeField()
    updated_at: pw.DateTimeField()

    class Meta:
        database = CpDb

# Create base model
base_models = [Attachment]