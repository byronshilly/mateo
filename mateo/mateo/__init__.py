from mateo.app import create_app



# Need to import models for Flask-Migrate to pick up
from mateo.models import (
    user,
    game,
    listing,
    shipment
)

# Need to import endpoints for Flask-Rebar to pick up
from mateo.api.v1 import (
    user,
    game,
    listing,
    shipment
)
