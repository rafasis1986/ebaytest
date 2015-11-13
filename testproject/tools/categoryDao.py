# -*- coding: utf-8 -*-
'''
Created on Nov 13, 2015

@author: rtorres
'''
from collections import OrderedDict

from tools.models import Category
from tools.simpleorm import BaseDao


class CreateCategory(BaseDao):
    sql = """CREATE TABLE categories (
            id INTEGER NOT NULL,
            name VARCHAR,
            level INTEGER,
            best_offer BOOLEAN,
            parent_id INTEGER NOT NULL,
            PRIMARY KEY (id),
            CHECK (best_offer IN (0, 1)),
            FOREIGN KEY(parent_id) REFERENCES categories (id)
        );"""


class CreateCategoryIndex(BaseDao):
    sql = "CREATE INDEX ix_category_id ON categories (id);"


class CreateCategoryParentIndex(BaseDao):
    sql = "CREATE INDEX ix_parent_id ON categories (parent_id);"


class DropCategory(BaseDao):
    sql = "DROP TABLE IF EXISTS categories;"


class InsertCategory(BaseDao):
    sql = """INSERT INTO categories (id, name, level, best_offer, parent_id)
            VALUES (?, ?, ?, ?, ?)"""


class SelectCategoryAll(BaseDao):
    sql = "SELECT C.id ,C.name, C.level, c.best_offer, C.parent_id FROM categories C "


if __name__ == '__main__':
    param = OrderedDict()
    result = SelectCategoryAll(dbfile='test.db', return_type=Category).execute(param)
    for elem in result:
        print(elem.id, elem.name, elem.level, elem.best_offer, elem.parent_id)

#===============================================================================
# if __name__ == '__main__':
#     result = DropCategory(dbfile = 'test.db').execute([])
#     result = CreateCategory(dbfile='test.db').execute([])
#     result = CreateCategoryIndex(dbfile = 'test.db').execute([])
#     result = CreateCategoryParentIndex(dbfile = 'test.db').execute([])
#     print('Rows affected:{}'.format(result))
#===============================================================================
#===============================================================================
# if __name__ == '__main__':
#     param = list()
#     for i in range(10000):
#         elem = OrderedDict()
#         elem['id'] = i
#         elem['name'] = '{}'.format(i)
#         elem['level'] = i%100
#         elem['best_offer'] = True
#         elem['parent_id'] = i
#         param.append(elem)
# 
#     result = InsertCategory (dbfile = 'test.db', commit_interval = 100, isolation_level = 'DEFERRED').execute(param)
#     print('Rows affected:{}'.format(result))
#===============================================================================
