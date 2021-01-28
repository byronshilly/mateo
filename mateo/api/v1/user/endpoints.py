from flask_rebar import errors

from uuid import UUID

from mateo.app import v1_registry, db, rebar
from mateo.models.user import User 
from mateo.schemas.user import (
    UserSchema,
    CreateUserSchema
)

from .utils import (
    _create_user
)


@v1_registry.handles(
    rule='/user/<uuid:user_id>',
    method='GET',
    response_body_schema=UserSchema()
)
def get_user(user_id: UUID):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        raise errors.NotFound()

    print(user)
    return user

@v1_registry.handles(
    rule='/user',
    method='POST',
    request_body_schema=CreateUserSchema(),
    response_body_schema=UserSchema()
)
def create_user():
    body = rebar.validated_body
    user = _create_user(body)
    return user

