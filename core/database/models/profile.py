from core.database.connect import CpDb
import peewee as pw
from core.database.models import attachments

class Profile(pw.Model):
    """
    User profile model, used to colorize user profile
    """
    id: int = pw.AutoField()
    first_name: str = pw.CharField(max_length=50, null=True)
    last_name: str = pw.CharField(max_length=50, null=True)
    position: str = pw.CharField(null=True)
    # Attachments
    avatar: attachments.Attachment = pw.ForeignKeyField(attachments.Attachment, null=True)
    banner: str = pw.TextField(null=True)
    # External information
    biography: str = pw.TextField(null=True)
    phone: str = pw.CharField(max_length=10, null=True)
    website: str = pw.CharField(max_length=255, null=True)

    class Meta:
        database = CpDb

# Create base model
base_models = [Profile]