# -*- coding: utf-8 -*-
'''
Created on Nov 13, 2015

@author: rtorres
'''
from tools.simpleorm import BaseDao


class CreateCategory(BaseDao):
    sql = """CREATE TABLE categories (
            id INTEGER NOT NULL,
            name VARCHAR,
            level INTEGER,
            best_offer BOOLEAN,
            parent_id INTEGER NOT NULL,
            PRIMARY KEY (id),
            CHECK (best_offer IN (0, 1))
        );"""


class CreateCategoryIndex(BaseDao):
    sql = "CREATE INDEX ix_category_id ON categories (id);"


class CreateCategoryParentIndex(BaseDao):
    sql = "CREATE INDEX ix_parent_id ON categories (parent_id);"


class DropCategory(BaseDao):
    sql = "DROP TABLE IF EXISTS categories;"


class InsertCategory(BaseDao):
    sql = """INSERT INTO categories (id, name, level, best_offer, parent_id)
            VALUES (?, ?, ?, ?, ?);"""


class SelectCategory(BaseDao):
    sql = """SELECT *  FROM categories where id=?; """


class SelectCategoryAll(BaseDao):
    sql = """SELECT * FROM categories; """


class SelectCategoriesChildren(BaseDao):
    sql = """SELECT * FROM categories WHERE parent_id = ? AND id != parent_id
            ORDER BY name ASC;"""
