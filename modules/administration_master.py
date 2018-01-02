#!/usr/bin/env python
# coding: utf8
from gluon import *

# grid function : company, branch, department, role, employee, bank, customer, supplier
def grid_0(table, create, editable, deletable, details, searchable, sortable, orderby, links, csv, 
		   showbuttontext, onvalidation, oncreate, onupdate, ondelete):
	grid = SQLFORM.grid(table, create = create, editable = editable, deletable = deletable, 
						details = details, searchable = searchable, sortable = sortable, 
						orderby = orderby, links = links, csv = csv, showbuttontext = showbuttontext, 
						onvalidation = onvalidation, oncreate = oncreate, onupdate = onupdate, 
						ondelete = ondelete)
	return locals()

# form function : modal
def form_0(table, fields, target_response):
	form = SQLFORM(table, fields = fields)
	if form.process(formname = 'form_modal').accepted:
		current.response.js = target_response
		redirect(current.request.env.http_web2py_component_location, client_side = True)
	elif form.errors:
		current.response.flash = 'form has errors'
	return dict(form = form)
