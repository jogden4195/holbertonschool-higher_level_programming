#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()


class State(Base):
    """ Class definition for State """
    __tablename__ = 'states'
    id = Column('id', Integer,
                nullable=False,
                primary_key=True,
                unique=True,
                autoincrement=True)
    name = Column('name', String(128), nullable=False)
    cities = relationship("City", backref=backref(
                          "states", cascade="all, delete"))
