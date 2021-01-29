from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields



"""
Response messages

"""
class ResponseMessages:
    GAME_ALREADY_EXISTS = "A game with this title already exists on this platform."
    GAME_DOESNT_EXIST = "This game doesn't exist."
    COULDNT_DELETE_GAME = "Something went wrong. This game couldn't be deleted."



"""
Response schemas

"""
class GameSchema(ResponseSchema):
    id = fields.String()
    title = fields.String()
    platform = fields.String()
    image = fields.Url(allow_none=True)



"""
Request schemas

"""
class GameByIdSchema(RequestSchema):
    id = fields.String(required=True)
    

class GameByTitleAndPlatformSchema(RequestSchema):
    title = fields.String(required=True)
    platform = fields.String(required=True)


class CreateGameSchema(RequestSchema):
    title = fields.String(required=True)
    platform = fields.String(required=True)
    image = fields.Url(required=False, default=None)
