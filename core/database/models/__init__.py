from core.database.connect import CpDb
from core.database.models import main, attachments, profile, posts

base_models = main.base_models + attachments.base_models + profile.base_models + posts.base_models

CpDb.create_tables(base_models)