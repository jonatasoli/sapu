from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()
    document = fields.TextField()
    mail = fields.TextField()
    oauth = fields.TextField()
    role_id = fields.IntField()

    def __str__(self):
        return self.name

