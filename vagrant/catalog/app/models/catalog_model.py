from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import uuid

from ..config.database_setup import Base

class CatalogModel(Base):
    __tablename__ = 'catalog_table'

    id = Column(String(32), primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {'name': self.name, 'id': uuid.uuid4(), }
