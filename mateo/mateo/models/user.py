from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4

from mateo.app import db



class User(db.Model):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(64), unique=True, nullable=False)
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(1024), nullable=False)
