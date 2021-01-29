from sqlalchemy import Column, String, Integer
from uuid import uuid4

from mateo.app import db



class Game(db.Model):
    __tablename__ = 'games'

    id = Column(String(64), primary_key=True, default=uuid4)
    title = Column(String(256), unique=False, nullable=False)
    platform = Column(String(64), unique=False, nullable=False)
    image = Column(String(1024), unique=False, nullable=True)
    listing_count = Column(Integer(), unique=False, nullable=False, default=0)
