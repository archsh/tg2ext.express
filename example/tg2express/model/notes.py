# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from tg2express.model import DeclarativeBase, metadata, DBSession
__all__ = ['DickNote', ]


class DickNote(DeclarativeBase):
    __tablename__ = 'db_dicknotes'

    #{ Columns
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(256), nullable=False)
    keys = Column(Unicode(256), nullable=True)
    content = Column(Text, nullable=True)
    created = Column(DateTime, default=func.NOW())
    #}
