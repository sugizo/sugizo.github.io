# -*- coding: utf-8 -*-

auth.requires_login()(lambda: None)()

# index
def index():
	return locals()

# language
def language():
	return locals()
