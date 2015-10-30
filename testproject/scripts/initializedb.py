# -*- coding: utf-8 -*-
'''
Created on Oct 28, 2015

@author: rtorres
'''
from sqlalchemy.engine import create_engine

from models import DBSession, Base
from tools.constants import DB_FILE
from tools.ebay import bulkCategories
import subprocess


def initDb():
    subprocess.call("rm *.html", shell=True)
    engine = create_engine('sqlite:///%s' % DB_FILE)
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    bulkCategories(engine)
