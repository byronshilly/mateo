from flask_rebar import errors
from flask_jwt import jwt_required, current_identity as current_user

from mateo.app import v1_registry, rebar
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


"""
Get a shipment 

"""
@v1_registry.handles(
    rule='/shipment/<uuid:shipment_id>',
    method='GET',
    response_body_schema=ShipmentSchema()
)
@jwt_required()
def get_shipment(shipment_id):
    shipment = _get_shipment(shipment_id)
    if not shipment:
        raise errors.NotFound(msg=ResponseMessages.SHIPMENT_DOESNT_EXIST)

    return shipment


"""
Create a new shipment 

"""
@v1_registry.handles(
    rule='/shipment',
    method='POST',
    request_body_schema=CreateShipmentSchema(),
    response_body_schema={201: ShipmentSchema()}
)
@jwt_required()
def create_shipment():
    body = rebar.validated_body
    shipment = _create_shipment(body)
    return (shipment, 201)


"""
Delete a shipment 

"""
@v1_registry.handles(
    rule='/shipment',
    method='DELETE',
    request_body_schema=ShipmentByIdSchema()
)
@jwt_required()
def delete_shipment():
    body = rebar.validated_body

    shipment = _get_shipment(body['id'])
    if not shipment:
        raise errors.NotFound(msg=ResponseMessages.SHIPMENT_DOESNT_EXIST)

    # Will return true if successful
    if not _delete_shipment(body['id']):
        raise errors.InternalError(msg=ResponseMessages.COULDNT_DELETE_SHIPMENT)

    return "", 204
