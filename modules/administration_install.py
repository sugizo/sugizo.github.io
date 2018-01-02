#!/usr/bin/env python
# coding: utf8

#import os
#print os.getcwd()

#import sys; 
#sys.path.append('project/python/web2py/')
#sys.path.append('../../../')

from gluon.contrib.webclient import WebClient

""" Install """
print "Install"

install = WebClient('http://127.0.0.1:8000/administration/install/',
					postbacks = True)

# run installation 
install.get('index')

if 'Installation Done' in install.text:
	print "Installation Done"
else:
	print "Installation Failed"

