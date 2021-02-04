from flask_rebar import errors
from flask_jwt_extended import jwt_required

from mateo.app import rebar
from mateo.models.game import Game
from mateo.schemas.game import (
    ResponseMessages,
    GameSchema,
    GameByIdSchema,
    CreateGameSchema
)

from .utils import (
    _get_game,
    _get_game_by_title_and_platform,
    _create_game,
    _delete_game
)



v1_game_registry = rebar.create_handler_registry(prefix='/api/v1/game')

@v1_game_registry.handles(
    rule='/<uuid:game_id>',
    method='GET',
    response_body_schema=GameSchema()
)
@jwt_required
def get_game(game_id):
    game = _get_game(game_id)
    if not game:
        raise errors.NotFound(msg=ResponseMessages.GAME_DOESNT_EXIST)

    return game


@v1_game_registry.handles(
    rule='/',
    method='POST',
    request_body_schema=CreateGameSchema(),
    response_body_schema={201: GameSchema()}
)
@jwt_required
def create_game():
    body = rebar.validated_body

    # Check if the game already exists
    game = _get_game_by_title_and_platform(body['title'], body['platform'])
    if game:
        raise errors.Conflict(msg=ResponseMessages.GAME_ALREADY_EXISTS)

    game = _create_game(body)
    return (game, 201)


@v1_game_registry.handles(
    rule='/',
    method='DELETE',
    request_body_schema=GameByIdSchema()
)
@jwt_required
def delete_game():
    body = rebar.validated_body

    game = _get_game(body['id'])
    if not game:
        raise errors.NotFound(msg=ResponseMessages.GAME_DOESNT_EXIST)

    # Will return true if successful
    if not _delete_game(body['id']):
        raise errors.InternalError(msg=ResponseMessages.COULDNT_DELETE_GAME)

    return "", 204

