from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, get_jwt_identity, jwt_refresh_token_required, set_refresh_cookies

import bcrypt
import secrets

from mateo.extensions import rebar
from mateo.schemas.auth import (
    GetTokenSchema
)



auth_registry = rebar.create_handler_registry(prefix='/auth')

@auth_registry.handles(
    rule='',
    method='POST',
    request_body_schema=GetTokenSchema()
)
def login():
    body = rebar.validated_body

    username = body['username'] 
    password = body['password'] 

    from mateo.models.user import User
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password, user.password):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        response = {
	    "access_token": access_token,
	    "refresh_token": refresh_token 
	}

        return response


@auth_registry.handles(
    rule='/refresh',
    method='POST',
)
@jwt_refresh_token_required
def refresh_token():
    current_user = get_jwt_identity()
    return { 'access_token': create_access_token(identity=current_user) }
