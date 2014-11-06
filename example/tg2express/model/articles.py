# -*- coding: utf-8 -*-
"""Sample model module."""

from sqlalchemy import *
from sqlalchemy.orm import mapper, relation
from sqlalchemy.orm import column_property
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.types import Integer, Unicode
#from sqlalchemy.orm import relation, backref

from tg2express.model import DeclarativeBase, metadata, DBSession
__all__ = ['Writer', 'Article', 'Comment']


class Writer(DeclarativeBase):
    __tablename__ = 'db_writers'
    #{ Columns
    id = Column(Integer, primary_key=True)
    firstname = Column(Unicode(64), nullable=False)
    lastname = Column(Unicode(64), nullable=False)
    gender = Column(Enum('Male', 'Female', name='wrtier_gender'), default='Male')
    birthday = Column(Date, nullable=True)
    description = Column(Text, nullable=True)
    created = Column(DateTime, default=func.NOW())
    #}
    fullname = column_property(firstname + " " + lastname)


class Article(DeclarativeBase):
    __tablename__ = 'db_articles'

    #{ Columns
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(256), nullable=False)
    keys = Column(Unicode(256), nullable=True)
    content = Column(Text, nullable=True)
    writer_id = Column(Integer, ForeignKey('db_writers.id'), nullable=False)
    created = Column(DateTime, default=func.NOW())
    #}
    writer = relation('Writer', backref='articles')


class Comment(DeclarativeBase):
    __tablename__ = 'db_comments'
    #{ Columns
    id = Column(Integer, primary_key=True)
    comment = Column(Unicode(256), nullable=False)
    article_id = Column(Integer, ForeignKey('db_articles.id'), nullable=False)
    created = Column(DateTime, default=func.NOW())
    #}
    db_articles = relation('Article', backref='comments')
