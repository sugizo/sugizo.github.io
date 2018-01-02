#!/usr/bin/env python
# coding: utf8
from gluon import *

# print function for print controller : receipt, invoice
def print_0(header_id):
    header = current.db(header_id == current.request.args(0)).select(cache = (current.cache.ram, 10)).first()
    return dict(header=header)
