# -*- coding: utf-8 -*-
'''
Created on Oct 28, 2015

@author: rtorres
'''
import subprocess

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session

from constants import XML_FILE
from models import Category
from tools.constants import DB_FILE
import xml.etree.ElementTree as ET


CATEGORY_STACK = list()


def getEbayCategories():
    return subprocess.call("scripts/get_categories.sh > %s" % XML_FILE,
                           shell=True)


def getCategoryTree(root):
    categories = list()
    flag = True
    rootTree = None
    min_level = 1
    delta_level = 0
    for child in root:
        if 'CategoryArray' in child.tag:
            for category in child:
                best_offer = bool(category[0].text)
                cat_id = int(category[2].text)
                level = int(category[3].text)
                name = category[4].text
                name = name.encode("ascii", "ignore")
                if flag:
                    rootTree = Category(cat_id=cat_id, name=name,
                                        best_offer=best_offer, level=level)
                    min_level = level
                    categories.append(rootTree)
                    flag = False
                else:
                    delta_level = level - min_level
                    if len(categories) > delta_level:
                        while(len(categories) > delta_level):
                            categories.pop()
                    parent = categories[-1]
                    aux = Category(cat_id=cat_id, name=name,
                                   best_offer=best_offer, level=level,
                                   parent=parent)
                    categories.append(aux)
            break
    return rootTree


def dropCategories(session):
    node = session.query(Category).filter(Category.parent == None).first()
    if node is not None:
        session.delete(node)
        session.commit()


def makeChildrenStack(node):
    children = [item for item in node.children]
    children.sort(reverse=True)
    for index in children:
        makeChildrenStack(node.children[index])
    CATEGORY_STACK.append(node)


def bulkCategories(engine):
    getEbayCategories()
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    session = Session(engine)
    dropCategories(session)
    node = getCategoryTree(root)
    session.add(node)
    session.commit()


def getTreeCategory(category_id):
    engine = create_engine('sqlite:///%s' % DB_FILE)
    session = Session(engine)
    node = session.query(Category).\
        filter(Category.id == category_id).first()
    if node is None:
        print("No category with ID: %s" % str(category_id))
    else:
        makeChildrenStack(node)
        while len(CATEGORY_STACK) > 0:
            print(CATEGORY_STACK.pop())
