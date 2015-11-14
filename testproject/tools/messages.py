# -*- coding: utf-8 -*-
'''
Created on Oct 30, 2015

@author: rtorres
'''


def avaliable_subcomands():
    print('\nAvailable subcommands:\n')
    print('\t--rebuild')
    print('\t--render #CATEGORY_ID')
    print('')


def unknow_command(arg=''):
    print("Unknown command: '%s'" % arg)
    print("Type 'testproject help' for usage.\n")


def need_category_id():
    print("Please submit one category id number.\n")


def invalid_category_id(arg=''):
    print("Your category id '%s' is in wrong format." % arg)
    need_category_id()
