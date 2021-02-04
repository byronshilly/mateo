from flask_rebar import errors
from flask_jwt_extended import jwt_required, get_jwt_identity 

from mateo.app import rebar
from mateo.models.listing import Listing
from mateo.schemas.listing import (
    ResponseMessages,
    ListingSchema,
    ListingByIdSchema,
    ListingBySellerIdSchema,
    CreateListingSchema,
    ModifyListingSchema
)

from .utils import (
    _get_listing,
    _get_listings_by_seller,
    _create_listing,
    _delete_listing,
    _modify_listing
)



v1_listing_registry = rebar.create_handler_registry(prefix='/api/v1/listing')


"""
Get a listing 

"""
@v1_listing_registry.handles(
    rule='/<uuid:listing_id>',
    method='GET',
    response_body_schema=ListingSchema()
)
@jwt_required
def get_listing(listing_id):
    listing = _get_listing(listing_id)
    if not listing:
        raise errors.NotFound(msg=ResponseMessages.LISTING_DOESNT_EXIST)

    return listing


"""
Get all listings for a user

"""
@v1_listing_registry.handles(
    rule='/',
    method='GET',
    request_body_schema=ListingBySellerIdSchema(),
    response_body_schema=ListingSchema(many=True)
)
@jwt_required
def get_listings():
    body = rebar.validated_body

    listings = _get_listings_by_seller(body['seller_id'])
    if not listings: 
        raise errors.NotFound(msg=ResponseMessages.USER_HAS_NO_LISTINGS)
    return listings


"""
Create a new listing 

"""
@v1_listing_registry.handles(
    rule='/',
    method='POST',
    request_body_schema=CreateListingSchema(),
    response_body_schema={201: ListingSchema()}
)
@jwt_required
def create_listing():
    body = rebar.validated_body
    listing = _create_listing(body)
    return (listing, 201)


"""
Delete a listing 

"""
@v1_listing_registry.handles(
    rule='/',
    method='DELETE',
    request_body_schema=ListingByIdSchema()
)
@jwt_required
def delete_listing():
    body = rebar.validated_body

    listing = _get_listing(body['id'])
    if not listing:
        raise errors.NotFound(msg=ResponseMessages.LISTING_DOESNT_EXIST)

    # Will return true if successful
    if not _delete_listing(body['id']):
        raise errors.InternalError(msg=ResponseMessages.COULDNT_DELETE_LISTING)

    return "", 204


"""
Update a listing's properties

Will be used for:
    - Marking a listing as sold by appending a buyer ID 
    - Marking a listing as shipped by appending shipment IDs

"""
@v1_listing_registry.handles(
    rule='//<uuid:listing_id>',
    method='PATCH',
    request_body_schema=ModifyListingSchema(),
    response_body_schema=ListingSchema()
)
@jwt_required
def modify_listing(listing_id):
    body = rebar.validated_body

    listing = _get_listing(listing_id)
    if not listing:
        raise errors.NotFound(msg=ResponseMessages.LISTING_DOESNT_EXIST)

    seller_id = str(listing.seller_id)
    if seller_id != get_jwt_identity():
        raise errors.Unauthorized(msg=ResponseMessages.LISTING_UNAUTHORIZED)

    return _modify_listing(listing, body) 
