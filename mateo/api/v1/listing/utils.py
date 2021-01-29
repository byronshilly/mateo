from flask_jwt import current_identity as current_user

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
    listing.seller_id = current_user.id
    listing.status = "LISTED"

    db.session.add(listing)
    db.session.commit()

    return listing


def _delete_listing(listing_id):
    listing = Listing.query.filter_by(id=listing_id).first()

    db.session.delete(listing)
    db.session.commit()

    return True
