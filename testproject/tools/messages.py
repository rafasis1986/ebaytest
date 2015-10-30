# -*- coding: utf-8 -*-
'''
Created on Oct 30, 2015

@author: rtorres
'''


def avaliableSubcomands():
    print('\nAvailable subcommands:\n')
    print('\t--rebuild')
    print('\t--render #CATEGORY_ID')
    print('')


def unknowCommand(arg=''):
    print("Unknown command: '%s'" % arg)
    print("Type 'testproject help' for usage.\n")


def needCategoryId():
    print("Please submit one category id number.\n")


def invalidCategoryId(arg=''):
    print("Your category id '%s' is in wrong format." % arg)
    needCategoryId()
