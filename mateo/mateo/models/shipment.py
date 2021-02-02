from sqlalchemy import Column, String, Numeric, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from mateo.app import db
from mateo.enums import ShipmentType


class Shipment(db.Model):
    __tablename__ = 'shipments'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    label = Column(String(1024), nullable=True)
    shipment_type = Column(Enum(ShipmentType), nullable=False) 
    from_addr = Column(String(1024), nullable=True)
    to_addr = Column(String(1024), nullable=True)
