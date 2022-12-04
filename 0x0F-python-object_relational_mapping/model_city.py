#!/usr/bin/python3
""" Defines a City model."""

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class City(Base):
    """Represents a city for a MySQL database.

    __tablename__(str): The name of the MySQL table to store States.
    state_id (sqlalchemy.Integer): The city's id.
    name (sqlalchemy.String): The city's name.
    """
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
