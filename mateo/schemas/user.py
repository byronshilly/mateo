from flask_rebar import ResponseSchema
from marshmallow import fields

class UserSchema(ResponseSchema):
    id = fields.String()
    email = fields.String()
