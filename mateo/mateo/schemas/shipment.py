from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields
from marshmallow_enum import EnumField

from mateo.enums import ShipmentType



"""
Response messages

"""
class ResponseMessages:
    SHIPMENT_DOESNT_EXIST = "This shipment doesn't exist."
    COULDNT_DELETE_SHIPMENT = "Something went wrong. This shipment couldn't be deleted."



"""
Response schemas

"""
class ShipmentSchema(ResponseSchema):
    id = fields.String()
    label = fields.String(allow_none=True)
    shipment_type = EnumField(ShipmentType)
    from_addr = fields.String(allow_none=True)
    to_addr = fields.String(allow_none=True)



"""
Request schemas

"""
class ShipmentByIdSchema(RequestSchema):
    id = fields.String(required=True)


class CreateShipmentSchema(RequestSchema):
    shipment_type = fields.String(required=True)
    from_addr = fields.String(required=True)
    to_addr = fields.String(required=True)
