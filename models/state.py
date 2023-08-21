#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state',
                          cascade='all, delete, save-update')

    @property
    def cities(self):
        """ getter - to get all state's cities """
        cities_found = [item for item in storage.all(City).values() if item.state_id == self.id]
        return cities_found
