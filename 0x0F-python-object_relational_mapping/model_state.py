#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ Class definition for State """
    __tablename__ = 'states'
    id = Column(Integer,
                nullable=False,
                primary_key=True,
                unique=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
