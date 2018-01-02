#!/usr/bin/env python
# coding: utf8

#import os
#print os.getcwd()

#import sys; 
#sys.path.append('project/python/web2py/')
#sys.path.append('../../../')

from gluon.contrib.webclient import WebClient

client = WebClient('http://127.0.0.1:8000/administration/',
                   postbacks = True)

client.get('default/index')

# login
data = dict(username = 'admin',
            password = 'password',
            _formname = 'login')
client.post('default/user/login', data = data)

assert('Admin' in client.text)

# master : bank
client.get('master/bank')

assert('Id' in client.text)

# logout
client.get('default/user/logout')
