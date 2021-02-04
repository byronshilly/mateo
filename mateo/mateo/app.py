from flask import Flask, jsonify
from flask_rebar import Rebar
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token, get_jwt_identity, jwt_refresh_token_required, set_refresh_cookies
from flask_cors import CORS

import bcrypt
import secrets

from mateo.extensions import rebar, db, migrate
from mateo.config import Config

# Need to import endpoints for Flask-Rebar to pick up
from mateo.api.v1 import (
    user,
    game,
    listing,
    shipment,
    auth
)

# Need to import models for Flask-Migrate to pick up
from mateo.models import (
    user,
    game,
    listing,
    shipment
)



# Application bootstrapping
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    rebar.init_app(app) 
    db.init_app(app)
    migrate.init_app(app)
    CORS(app)

    jwt = JWTManager(app)

    return app



# Auth endpoints
# from mateo.schemas.auth import (
#     AuthSchema,
#     GetTokenSchema
# )
# 
# @app.route('/auth', methods=['POST'])
# def login():
#     username = request.json.get('username', None)
#     password = request.json.get('password', None)
# 
#     from mateo.models.user import User
#     user = User.query.filter_by(username=username).first()
#     if user and bcrypt.checkpw(password, user.password):
#         access_token = create_access_token(identity=user.id)
#         refresh_token = create_refresh_token(identity=user.id)
# 
#         response = jsonify({"access_token": access_token})
#         set_refresh_cookies(response, create_refresh_token(identity=user.id))
#         return response, 200
# 
# 
# @auth_registry.handles(
#     rule='/refresh',
#     method='POST',
# )
# @jwt_refresh_token_required
# def refresh_token():
#     current_user = get_jwt_identity()
#     return { 'access_token': create_access_token(identity=current_user) }

