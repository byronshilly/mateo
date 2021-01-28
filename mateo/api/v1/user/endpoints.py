from flask_rebar import errors

from uuid import UUID

from mateo.app import registry 
from mateo.models.user import User 
from mateo.schemas.user import UserSchema


@registry.handles(
    rule="/user/<uuid:user_id>",
    method="GET",
    response_body_schema=UserSchema()
)
def get_user(user_id: UUID):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        raise errors.NotFound()

    return user
