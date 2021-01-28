from flask import Flask
from flask_rebar import Rebar
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from mateo.config import Config

# Flask Rebar 
rebar = Rebar() 
v1_registry = rebar.create_handler_registry(prefix='/api/v1/')

# Database
db = SQLAlchemy()
migrate = Migrate(db=db)

def create_app(): 
    app = Flask(__name__)
    app.config.from_object(Config)

    rebar.init_app(app) 
    db.init_app(app)
    migrate.init_app(app)

    return app 

if __name__ == '__main__':
    create_app().run()
