from datetime import datetime
from motorodm import (
    Document,
    StringField,
    ListField,
    DateTimeField
)


class User(Document):
    primary_email = StringField(db_name='primaryEmail', required=True, unique=True)
    password = StringField(required=True)
    secondary_emails = ListField(db_name='secondaryEmails', item_field=StringField())
    given_names = ListField(db_name='givenNames', item_field=StringField())
    family_name = StringField(db_name='familyName')
    nickname = StringField()
    created = DateTimeField(required=True)
    updated = DateTimeField(required=True)

    def before_create(self):
        self.created = self.updated = datetime.utcnow()

    def before_update(self):
        self.updated = datetime.utcnow()
