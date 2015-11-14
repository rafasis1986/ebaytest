#!/usr/bin/env python
'''
Created on Oct 30, 2015

@author: rtorres
'''
from exceptions import IndexError
import sys

from tools.ebay import make_tree_category
from tools.initializedb import init_db
from tools.messages import invalid_category_id, need_category_id, \
    avaliable_subcomands, unknow_command


def main(argv=sys.argv):
    if len(argv) > 1:
        if (argv[1] == '--rebuild'):
            init_db()
        elif (argv[1] == '--render'):
            try:
                make_tree_category(int(argv[2]))
            except ValueError:
                invalid_category_id(argv[2])
            except IndexError:
                need_category_id()
        elif (argv[1] == 'help'):
            avaliable_subcomands()
        else:
            unknow_command(argv[1])
    else:
        unknow_command()

if __name__ == '__main__':
    main(sys.argv)
