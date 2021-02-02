from flask_rebar import ResponseSchema, RequestSchema
from marshmallow import fields



"""
Response messages

"""
class ResponseMessages:
    LISTING_DOESNT_EXIST = "This listing doesn't exist."
    COULDNT_DELETE_LISTING = "Something went wrong. This listing couldn't be deleted."
    USER_HAS_NO_LISTINGS = "No listings were found for this user."
    LISTING_UNAUTHORIZED = "You are not authorized to modify this listing."



"""
Response schemas

"""
class ListingSchema(ResponseSchema):
    id = fields.String()
    game_id = fields.String()
    price = fields.Number()
    seller_id = fields.String()
    buyer_id = fields.String(allow_none=True)
    status = fields.String()
    b_shipment_id = fields.String(allow_none=True)
    s_shipment_id = fields.String(allow_none=True)



"""
Request schemas

"""
class ListingByIdSchema(RequestSchema):
    id = fields.String(required=True)


class ListingBySellerIdSchema(RequestSchema):
    seller_id = fields.String(required=True)
    

class CreateListingSchema(RequestSchema):
    game_id = fields.String(required=True)
    price = fields.Decimal(places=2)

class ModifyListingSchema(RequestSchema):
    price = fields.Number()
    buyer_id = fields.String()
    status = fields.String()
    b_shipment_id = fields.String()
    s_shipment_id = fields.String()
