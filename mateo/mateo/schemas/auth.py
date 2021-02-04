from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields



"""
Response schemas

"""
class AuthSchema(ResponseSchema):
    access_token = fields.String()


"""
Request schemas

"""
class GetTokenSchema(RequestSchema):
    username = fields.String(required=True)
    password = fields.String(required=True)
