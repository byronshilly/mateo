from flask_rebar import errors

from uuid import UUID

from mateo.app import v1_registry, rebar
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



@v1_registry.handles(
    rule='/game/<uuid:game_id>',
    method='GET',
    response_body_schema=GameSchema()
)
def get_game(game_id: UUID):
    game = _get_game(game_id)
    if not game:
        raise errors.NotFound(msg=ResponseMessages.GAME_DOESNT_EXIST)

    return game


@v1_registry.handles(
    rule='/game',
    method='POST',
    request_body_schema=CreateGameSchema(),
    response_body_schema={201: GameSchema()}
)
def create_game():
    body = rebar.validated_body

    # Check if the game already exists
    game = _get_game_by_title_and_platform(body['title'], body['platform'])
    if game:
        raise errors.Conflict(msg=ResponseMessages.GAME_ALREADY_EXISTS)

    game = _create_game(body)
    return (game, 201)


@v1_registry.handles(
    rule='/game',
    method='DELETE',
    request_body_schema=GameByIdSchema()
)
def delete_game():
    body = rebar.validated_body

    game = _get_game(body['id'])
    if not game:
        raise errors.NotFound(msg=ResponseMessages.GAME_DOESNT_EXIST)

    # Will return true if successful
    if not _delete_game(body['id']):
        raise errors.InternalError(msg=ResponseMessages.COULDNT_DELETE_GAME)

    return "", 204

