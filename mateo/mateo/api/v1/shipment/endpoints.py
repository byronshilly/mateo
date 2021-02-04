from flask_rebar import errors
from flask_jwt_extended import jwt_required, get_jwt_identity

from mateo.app import rebar
from mateo.models.shipment import Shipment
from mateo.schemas.shipment import (
    ResponseMessages,
    ShipmentSchema,
    ShipmentByIdSchema,
    CreateShipmentSchema
)

from .utils import (
    _get_shipment,
    _create_shipment,
    _delete_shipment
)



v1_shipment_registry = rebar.create_handler_registry(prefix='/api/v1/shipment')


"""
Get a shipment 

"""
@v1_shipment_registry.handles(
    rule='/<uuid:shipment_id>',
    method='GET',
    response_body_schema=ShipmentSchema()
)
@jwt_required
def get_shipment(shipment_id):
    shipment = _get_shipment(shipment_id)
    if not shipment:
        raise errors.NotFound(msg=ResponseMessages.SHIPMENT_DOESNT_EXIST)

    return shipment


"""
Create a new shipment 

"""
@v1_shipment_registry.handles(
    rule='/',
    method='POST',
    request_body_schema=CreateShipmentSchema(),
    response_body_schema={201: ShipmentSchema()}
)
@jwt_required
def create_shipment():
    body = rebar.validated_body
    shipment = _create_shipment(body)
    return (shipment, 201)


"""
Delete a shipment 

"""
@v1_shipment_registry.handles(
    rule='/',
    method='DELETE',
    request_body_schema=ShipmentByIdSchema()
)
@jwt_required
def delete_shipment():
    body = rebar.validated_body

    shipment = _get_shipment(body['id'])
    if not shipment:
        raise errors.NotFound(msg=ResponseMessages.SHIPMENT_DOESNT_EXIST)

    # Will return true if successful
    if not _delete_shipment(body['id']):
        raise errors.InternalError(msg=ResponseMessages.COULDNT_DELETE_SHIPMENT)

    return "", 204
