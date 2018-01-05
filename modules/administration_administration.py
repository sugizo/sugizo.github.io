#!/usr/bin/env python
# coding: utf8
from gluon import *

# form function : modal
def form_0(table, fields, target_response):
	form = SQLFORM(table, fields = fields)
	if form.process(formname = 'form_modal').accepted:
		current.response.js = target_response
		redirect(current.request.env.http_web2py_component_location, client_side = True)
	elif form.errors:
		current.response.flash = 'form has errors'
	return dict(form = form)

# form function : acknowledgement_of_work_result, official_travel
def form_1(table, fields, onvalidation, report):
	form = SQLFORM(table, fields = fields)
	if form.process(onvalidation = onvalidation).accepted:
		current.session.flash = current.T('Record Inserted')
		redirect(URL('report', report) )
	return dict(form = form)
