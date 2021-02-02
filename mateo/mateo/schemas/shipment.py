from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields



"""
Response messages

"""
class ResponseMessages:
    LISTING_DOESNT_EXIST = "This listing doesn't exist."
    COULDNT_DELETE_LISTING = "Something went wrong. This listing couldn't be deleted."
    USER_HAS_NO_LISTINGS = "No listings were found for this user."



"""
Response schemas

"""
class ShipmentSchema(ResponseSchema):
    id = fields.String()
    label = fields.String(allow_none=True)
    shipment_type = fields.String()
    from_addr = fields.String(allow_none=True)
    to_addr = fields.String(allow_none=True)



"""
Request schemas

"""
class ShipmentByIdSchema(RequestSchema):
    id = fields.String(required=True)
