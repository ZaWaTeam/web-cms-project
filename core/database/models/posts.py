from datetime import date
from typing import List, Literal, Optional
import peewee as pw
from core.database.connect import CpDb
from core.database.models.attachments import Attachment
from core.database.models.main import Groups, UserModel

class Category(pw.Model):
    id: int = pw.AutoField()
    title: str = pw.CharField(50)
    slug: str = pw.CharField(50)
    description: str = pw.CharField(300)
    thumbnail: Optional[Attachment] = pw.ForeignKeyField(Attachment, null=True)
    
    class Meta:
        database = CpDb

class Post(pw.Model):
    id: int = pw.AutoField()
    title: str = pw.CharField(255)
    content: str = pw.TextField(null=False)
    thumbnails: List[Attachment] = pw.ManyToManyField(Attachment)
    is_editor: bool = pw.BooleanField(default=False)
    slug: str = pw.CharField(max_length=30)
    category: Category = pw.ForeignKeyField(Category, null=True)
    # Settings & Additional Infos
    allow_comments: bool = pw.BooleanField(default=True)
    allow_comment_perms: List[str] = pw.TextField(null=True)
    allow_comment_groups: List[Groups] = pw.ManyToManyField(Groups)
    allow_comment_groups_empty_nobody: bool = pw.BooleanField()
    # Author
    author: UserModel = pw.ForeignKeyField(UserModel)
    edited_by: UserModel = pw.ForeignKeyField(UserModel)
    hide_author: bool = pw.BooleanField()
    # Status & Permissions
    status: Literal["draft", "moderation", "published", "cancled", "delayed"] = pw.CharField(15)
    access_groups: List[Groups] =  pw.ManyToManyField(Groups)
    # Date
    created_at: date = pw.DateTimeField()
    updated_at: date = pw.DateTimeField(null=True)

    class Meta:
        database = CpDb


class PostMeta(pw.Model):
    id: int = pw.AutoField()
    name: str = pw.CharField(50)
    post: Post = pw.ForeignKeyField(Post)

    class Meta:
        database = CpDb

# Create all models
base_models = [PostMeta, Post, Category]