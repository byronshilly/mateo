from flask_rebar import errors
from flask_jwt import jwt_required, current_identity

from mateo.app import v1_registry, rebar
from mateo.models.user import User 
from mateo.schemas.user import (
    ResponseMessages,
    UserSchema,
    UserByIdSchema,
    CreateUserSchema,
)

from .utils import (
    _get_user,
    _get_user_by_email,
    _create_user,
    _delete_user
)


@v1_registry.handles(
    rule='/user/<uuid:user_id>',
    method='GET',
    response_body_schema=UserSchema()
)
@jwt_required()
def get_user(user_id):
    user = _get_user(user_id)
    if not user:
        raise errors.NotFound(msg=ResponseMessages.USER_DOESNT_EXIST)

    return user


@v1_registry.handles(
    rule='/user',
    method='POST',
    request_body_schema=CreateUserSchema(),
    response_body_schema={201: UserSchema()}
)
def create_user():
    body = rebar.validated_body

    # Check if the email is taken
    user = _get_user_by_email(body['email'])
    if user: 
        raise errors.Conflict(msg=ResponseMessages.USER_ALREADY_EXISTS)

    user = _create_user(body)
    return (user, 201)


@v1_registry.handles(
    rule='/user',
    method='DELETE',
    request_body_schema=UserByIdSchema()
)
@jwt_required()
def delete_user():
    body = rebar.validated_body

    user = _get_user(body['id'])
    if not user:
        raise errors.NotFound(msg=ResponseMessages.USER_DOESNT_EXIST)

    # Will return true if successful
    if not _delete_user(body['id']):
        raise errors.InternalError(msg=ResponseMessages.COULDNT_DELETE_USER)

    return "", 204 
