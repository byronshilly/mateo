from flask_jwt_extended import get_jwt_identity

from mateo.app import db
from mateo.models.listing import Listing



def _get_listing(listing_id):
    listing = Listing.query.filter_by(id=listing_id).first()
    return listing


def _get_listings_by_seller(seller_id):
    listings = Listing.query.filter_by(seller_id=seller_id).all()
    return listings


def _create_listing(body):
    listing = Listing(**body)
    listing.seller_id = get_jwt_identity()
    listing.status = "LISTED"

    db.session.add(listing)
    db.session.commit()

    return listing


def _delete_listing(listing_id):
    listing = Listing.query.filter_by(id=listing_id).first()

    db.session.delete(listing)
    db.session.commit()

    return True


def _modify_listing(listing, body):
    for key in body:
        setattr(listing, key, body[key]) 

    db.session.add(listing)
    db.session.commit()

    return listing
