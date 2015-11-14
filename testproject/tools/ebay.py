# -*- coding: utf-8 -*-
'''
Created on Oct 28, 2015

@author: rtorres
'''
from collections import OrderedDict
import subprocess

from constants import XML_FILE
from models import Category
from tools.categoryDao import InsertCategory, DropCategory, SelectCategory, \
    SelectCategoriesChildren, CreateCategory, CreateCategoryIndex, \
    CreateCategoryParentIndex
from tools.constants import DB_FILE
from tools.html import make_html_file
import xml.etree.ElementTree as ET


def get_ebay_categories():
    return subprocess.call("scripts/get_categories.sh > %s" % XML_FILE,
                           shell=True)


def get_category_list(root):
    categories = list()
    for child in root:
        if 'CategoryArray' in child.tag:
            for category in child:
                for item in category:
                        if 'BestOfferEnabled' in item.tag:
                            best_offer = bool(item.text)
                        elif 'CategoryID' in item.tag:
                            id = int(item.text)
                        elif 'CategoryLevel' in item.tag:
                            level = int(item.text)
                        elif 'CategoryName' in item.tag:
                            name = str(item.text)
                        elif 'CategoryParentID' in item.tag:
                            parent_id = int(item.text)
                cat = OrderedDict()
                cat['id'] = id
                cat['name'] = name
                cat['level'] = level
                cat['best_offer'] = best_offer
                cat['parent_id'] = parent_id
                categories.append(cat)
            break
    return categories


def drop_all_categories():
    DropCategory(dbfile=DB_FILE).execute([])


def make_children_stack(category, stack=[]):
    param = OrderedDict()
    param['parent_id'] = category.id
    result = SelectCategoriesChildren(dbfile=DB_FILE, return_type=Category).execute(param)
    for catAux in result:
        make_children_stack(catAux, stack)
    stack.append(category)


def bulk_categories():
    get_ebay_categories()
    tree = ET.parse(XML_FILE)
    root = tree.getroot()
    DropCategory(dbfile=DB_FILE).execute([])
    CreateCategory(dbfile=DB_FILE).execute([])
    CreateCategoryIndex(dbfile=DB_FILE).execute([])
    CreateCategoryParentIndex(dbfile=DB_FILE).execute([])
    categories = get_category_list(root)
    result = InsertCategory(dbfile=DB_FILE, commit_interval=100,
                            isolation_level='DEFERRED').execute(categories)
    return result


def make_tree_category(category_id):
    stack = list()
    param = OrderedDict()
    param['id'] = category_id
    result = SelectCategory(dbfile='test.db', return_type=Category).execute(param)
    if len(result) == 0:
        print("No category with ID: %s" % str(category_id))
    else:
        make_children_stack(result.pop(), stack)
        make_html_file(stack)
