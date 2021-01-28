from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields

class UserSchema(ResponseSchema):
    id = fields.String()
    email = fields.String()

class CreateUserSchema(RequestSchema):
    email = fields.String(required=True)
