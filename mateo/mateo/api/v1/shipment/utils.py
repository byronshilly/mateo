from flask_jwt_extended import get_jwt_identity

from mateo.app import db
from mateo.models.shipment import Shipment
from mateo.enums import ShipmentType



def _get_shipment(shipment_id):
    shipment = Shipment.query.filter_by(id=shipment_id).first()
    return shipment


def _create_shipment(body):
    shipment = Shipment(**body)

    db.session.add(shipment)
    db.session.commit()

    return shipment


def _delete_shipment(shipment_id):
    shipment = Shipment.query.filter_by(id=shipment_id).first()

    db.session.delete(shipment)
    db.session.commit()

    return True
