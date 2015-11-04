# -*- coding: utf-8 -*-
'''
Created on Oct 30, 2015

@author: rtorres
'''
from jinja2.environment import Environment
from jinja2.loaders import FileSystemLoader


def makeHtmlFile(stack):
    root = stack[-1]
    stack.reverse()
    j2_env = Environment(loader=FileSystemLoader('templates'),
                         trim_blocks=True)
    with open("%s.html" % root.id, "wb") as fh:
        fh.write(j2_env.get_template('default.html'). \
             render(title="Category %s" % root.id,
                    stack=stack,
                    name=root.name,).encode('utf-8'))
