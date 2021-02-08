from flask import make_response
from flask_jwt_extended import (
    create_access_token, 
    create_refresh_token, 
    get_jwt_identity, 
    jwt_refresh_token_required, 
    set_access_cookies,
    set_refresh_cookies,
    get_csrf_token,
    unset_jwt_cookies
)

import bcrypt
import secrets

from mateo.extensions import rebar
from mateo.models.user import User
from mateo.schemas.auth import (
    GetTokenSchema
)



auth_registry = rebar.create_handler_registry(prefix='/auth')

@auth_registry.handles(
    rule='/login',
    method='POST',
    request_body_schema=GetTokenSchema()
)
def login():
    body = rebar.validated_body

    username = body['username'] 
    password = body['password'] 

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(password, user.password):
        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        response_body = {
            'login': True,
            'access_csrf_token': get_csrf_token(access_token),
            'refresh_csrf_token': get_csrf_token(refresh_token)
	}

        response = make_response(response_body)
        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return response
    else: 
        return {'login': False}, 401


@auth_registry.handles(
    rule='/refresh',
    method='POST',
)
@jwt_refresh_token_required
def refresh_token():
    current_user = get_jwt_identity()

    access_token = create_access_token(identity=current_user) 

    response_body = {
        'refresh': True,
        'access_csrf_token': get_csrf_token(access_token)
    }

    response = make_response(response_body)
    set_access_cookies(response, access_token)

    return response


@auth_registry.handles(
    rule='/logout',
    method='POST'
)
def logout():
    response_body = {
        'logout': True
    }

    response = make_response(response_body)
    unset_jwt_cookies(response)

    return response




