from datetime import datetime
from motorodm import (
    Document,
    StringField,
    ListField,
    DateTimeField,
    ReferenceField
)

from .user import User


class Permission(Document):
    user = ReferenceField(reference_document_type=User, required=True, unique=True)
    roles = ListField(item_field=StringField(), required=True)
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)

    def before_create(self):
        self.created = self.updated = datetime.utcnow()

    def before_update(self):
        self.updated = datetime.utcnow()
