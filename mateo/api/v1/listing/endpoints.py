from flask_rebar import errors
from flask_jwt import jwt_required

from mateo.app import v1_registry, rebar
from mateo.models.listing import Listing
from mateo.schemas.listing import (
    ResponseMessages,
    ListingSchema,
    ListingByIdSchema,
    ListingBySellerIdSchema,
    CreateListingSchema
)

from .utils import (
    _get_listing,
    _get_listings_by_seller,
    _create_listing,
    _delete_listing
)



@v1_registry.handles(
    rule='/listing/<uuid:listing_id>',
    method='GET',
    response_body_schema=ListingSchema()
)
@jwt_required()
def get_listing(listing_id):
    listing = _get_listing(listing_id)
    if not listing:
        raise errors.NotFound(msg=ResponseMessages.LISTING_DOESNT_EXIST)

    return listing


@v1_registry.handles(
    rule='/listing',
    method='GET',
    request_body_schema=ListingBySellerIdSchema(),
    response_body_schema=ListingSchema(many=True)
)
@jwt_required()
def get_listings():
    body = rebar.validated_body

    listings = _get_listings_by_seller(body['seller_id'])
    return listings


@v1_registry.handles(
    rule='/listing',
    method='POST',
    request_body_schema=CreateListingSchema(),
    response_body_schema={201: ListingSchema()}
)
@jwt_required()
def create_listing():
    body = rebar.validated_body
    listing = _create_listing(body)
    return (listing, 201)


@v1_registry.handles(
    rule='/listing',
    method='DELETE',
    request_body_schema=ListingByIdSchema()
)
@jwt_required()
def delete_listing():
    body = rebar.validated_body

    listing = _get_listing(body['id'])
    if not listing:
        raise errors.NotFound(msg=ResponseMessages.LISTING_DOESNT_EXIST)

    # Will return true if successful
    if not _delete_listing(body['id']):
        raise errors.InternalError(msg=ResponseMessages.COULDNT_DELETE_LISTING)

    return "", 204

