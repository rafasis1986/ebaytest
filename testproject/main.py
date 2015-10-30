#!/usr/bin/env python
'''
Created on Oct 30, 2015

@author: rtorres
'''
import sys

from scripts.initializedb import initDb
from tools.ebay import getTreeCategory
from tools.messages import avaliableSubcomands, unknowCommand, needCategoryId,\
    invalidCategoryId
from exceptions import IndexError


def main(argv=sys.argv):
    if len(argv) > 1:
        if (argv[1] == '--rebuild'):
            initDb()
        elif (argv[1] == '--render'):
            try:
                getTreeCategory(int(argv[2]))
            except ValueError:
                invalidCategoryId(argv[2])
            except IndexError:
                needCategoryId()
        elif (argv[1] == 'help'):
            avaliableSubcomands()
        else:
            unknowCommand(argv[1])
    else:
        unknowCommand()

if __name__ == '__main__':
    main(sys.argv)
