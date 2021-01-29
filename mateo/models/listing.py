from sqlalchemy import Column, String, Numeric, ForeignKey
from uuid import uuid4

from mateo.app import db



class Listing(db.Model):
    __tablename__ = 'listings'

    id = Column(String(64), primary_key=True, default=uuid4)
    game_id = Column(String(64), ForeignKey('games.id'), nullable=False)
    price = Column(Numeric(5, 2), nullable=False)
    seller_id = Column(String(64), ForeignKey('users.id'), nullable=False)
    buyer_id = Column(String(64), ForeignKey('users.id'), nullable=True)
    status = Column(String(64), nullable=False)
    # BYRON - Need to uncomment once the shipment table is created
    # s_shipment_id = Column(UUID(as_uuid=True), ForeignKey('shipment.id'), nullable=True)
    # b_shipment_id = Column(UUID(as_uuid=True), ForeignKey('shipment.id'), nullable=True)

