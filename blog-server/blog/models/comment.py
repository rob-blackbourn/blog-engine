from datetime import datetime
from motorodm import (
    Document,
    StringField,
    DateTimeField,
    ReferenceField
)

from .post import Post


class Comment(Document):
    post = ReferenceField(reference_document_type=Post, required=True, unique=True)
    previous = ReferenceField(reference_document_type=lambda: Comment, required=True, unique=True)
    content_type = StringField(required=True)
    content = StringField(required=True)
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)

    def before_create(self):
        self.created = self.updated = datetime.utcnow()

    def before_update(self):
        self.updated = datetime.utcnow()
