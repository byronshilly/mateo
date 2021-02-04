from flask_rebar import Rebar
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

rebar = Rebar()
db = SQLAlchemy()
migrate = Migrate(db=db)
