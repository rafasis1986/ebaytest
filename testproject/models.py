# -*- coding: utf-8 -*-
'''
Created on Oct 28, 2015

@author: rtorres
'''
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.orm.scoping import scoped_session
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Boolean


DBSession = scoped_session(sessionmaker())
Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    level = Column(Integer, default=1)
    best_offer = Column(Boolean)
    parent_id = Column(Integer, ForeignKey(id))
    children = relationship("Category",
                            cascade="all, delete-orphan",
                            backref=backref("parent", remote_side=id),
                            collection_class=attribute_mapped_collection('name')
                            )

    def __init__(self, cat_id=None, name=None, best_offer=True, level=1,
                 parent=None):
        self.id = cat_id
        self.name = name
        self.best_offer = best_offer
        self.level = level
        self.parent = parent

    def __repr__(self):
        return '<Category(%s#%s)>' % (self.__class__.__name__, self.id)

    def __str__(self):
        return "%s %s" % (self.id, self.name)
