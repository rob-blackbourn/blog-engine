from datetime import datetime
from motorodm import (
    Document,
    StringField,
    DateTimeField,
    ReferenceField
)

from .user import User


class Blog(Document):
    owner = ReferenceField(reference_document_type=User, required=True, unique=True)
    title = StringField(required=True, unique=True)
    content_type = StringField(required=True)
    content = StringField()
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)

    def before_create(self):
        self.created = self.updated = datetime.utcnow()

    def before_update(self):
        self.updated = datetime.utcnow()
