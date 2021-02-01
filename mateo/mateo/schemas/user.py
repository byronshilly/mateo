from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields



"""
Response messages

"""
class ResponseMessages:
    USER_ALREADY_EXISTS = "A user with this email already exists."
    USER_DOESNT_EXIST = "This user doesn't exist."
    COULDNT_DELETE_USER = "Something went wrong. This user couldn't be deleted."



"""
Response schemas

"""
class UserSchema(ResponseSchema):
    id = fields.String()
    email = fields.String()
    username = fields.String()



"""
Request schemas

"""
class UserByIdSchema(RequestSchema):
    id = fields.String(required=True)


class CreateUserSchema(RequestSchema):
    email = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)
