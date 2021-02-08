from flask import Flask, jsonify
from flask_rebar import Rebar
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from mateo.extensions import rebar, db, migrate
from mateo.config import Config

# Need to import endpoints for Flask-Rebar to pick up
from mateo.api.v1 import (
    user,
    game,
    listing,
    shipment
)

# Need to import models for Flask-Migrate to pick up
from mateo.models import (
    user,
    game,
    listing,
    shipment
)

# Import auth endpoints
from mateo.auth import auth_registry



# Application bootstrapping
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    rebar.init_app(app) 
    db.init_app(app)
    migrate.init_app(app)
    CORS(app, resources={r"/*": {"origins": "http://localhost:8000"}}, supports_credentials=True)
    jwt = JWTManager(app)

    return app
