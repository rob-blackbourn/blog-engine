from datetime import datetime
from motorodm import (
    Document,
    StringField,
    DateTimeField,
    ReferenceField
)

from .blog import Blog


class Post(Document):
    blog = ReferenceField(reference_document_type=Blog, required=True, unique=True)
    title = StringField(required=True, unique=True)
    status = StringField(required=True, default='draft')
    content_type = StringField(required=True)
    content = StringField()
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)

    def before_create(self):
        self.created = self.updated = datetime.utcnow()

    def before_update(self):
        self.updated = datetime.utcnow()
