# -*- coding: utf-8 -*-

import administration_master

auth.requires_login()(lambda: None)()

create = True
editable = has_membership_admin
deletable = has_membership_admin
details = True
searchable = True
sortable = True
links = None
csv = True
showbuttontext = False
onvalidation = None
oncreate = None
onupdate = None
ondelete = None

# user
def user():
	table = db.auth_user
	orderby = ~table.id
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
									    sortable, orderby, links, csv, showbuttontext, onvalidation, 
									    oncreate, onupdate, ondelete)

# group
def group():
	table = db.auth_group
	orderby = ~table.id
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
									    sortable, orderby, links, csv, showbuttontext, onvalidation, 
									    oncreate, onupdate, ondelete)

# membership
def membership():
	table = db.auth_membership
	orderby = ~table.id
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
									    sortable, orderby, links, csv, showbuttontext, onvalidation, 
									    oncreate, onupdate, ondelete)

# permission
def permission():
	table = db.auth_permission
	orderby = ~table.id
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
									    sortable, orderby, links, csv, showbuttontext, onvalidation, 
									    oncreate, onupdate, ondelete)

# event
def event():
	table = db.auth_event
	orderby = ~table.id
	oncreate = partial(administration_event.oncreate_event, table = 'auth_event')
	onupdate = partial(administration_event.onupdate_event, table = 'auth_event')
	ondelete = administration_event.ondelete_event
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
									    sortable, orderby, links, csv, showbuttontext, onvalidation, 
									    oncreate, onupdate, ondelete)

# index
def index():
	return locals()

""" modal """
# modal_auth_user
def modal_auth_user():
	table = db.auth_user
	fields = None
	target_response = '(function($) {$("#modal_auth_user").modal("hide");}(jQuery));'
	return administration_master.form_0(table, fields, target_response)

# modal_bank
def modal_bank():
	table = db.bank
	fields = None
	target_response = '(function($) {$("#modal_bank").modal("hide");}(jQuery));'
	return administration_master.form_0(table, fields, target_response)

# modal_company
def modal_company():
	table = db.company
	fields = None
	target_response = '(function($) {$("#modal_company").modal("hide");}(jQuery));'
	return administration_master.form_0(table, fields, target_response)

# modal_department
def modal_department():
	table = db.department
	fields = None
	target_response = '(function($) {$("#modal_department").modal("hide");}(jQuery));'
	return administration_master.form_0(table, fields, target_response)

# modal_role
def modal_role():
	table = db.role
	fields = None
	target_response = '(function($) {$("#modal_role").modal("hide");}(jQuery));'
	return administration_master.form_0(table, fields, target_response)

# modal_branch
def modal_branch():
	table = db.branch
	fields = None
	target_response = '(function($) {$("#modal_branch").modal("hide");}(jQuery));'
	return administration_master.form_0(table, fields, target_response)

# company
def company():
	table = db.company
	orderby = ~table.id
	links = [dict(header = T('Logo'), 
				  body = lambda row: A(IMG(_src = URL('default', 'download', args = row.logo), 
										_width = 100, _height = 100), 
										_href = URL('default', 'download', args = row.logo) ) ) ]
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
										sortable, orderby, links, csv, showbuttontext, onvalidation, 
										oncreate, onupdate, ondelete)

# branch
def branch():
	table = db.branch
	orderby = ~table.id
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
										sortable, orderby, links, csv, showbuttontext, onvalidation, 
										oncreate, onupdate, ondelete)

# department
def department():
	table = db.department
	orderby = ~table.id
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
										sortable, orderby, links, csv, showbuttontext, onvalidation, 
										oncreate, onupdate, ondelete)

# role
def role():
	table = db.role
	orderby = ~table.id
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
										sortable, orderby, links, csv, showbuttontext, onvalidation, 
										oncreate, onupdate, ondelete)

# onvalidation_employee
def __onvalidation_employee(form):
	if form.vars.is_auth == 'on':
		if form.vars.auth_user:
			row = db(db.auth_user.id == form.vars.auth_user).select().first()

			form.vars.username = row.username
			form.vars.first_name = row.first_name
			form.vars.last_name = row.last_name
			form.vars.email = row.email
		else:
			form.errors.auth_user = T('Enter a value')
	else:
		if not form.vars.first_name:
			form.errors.first_name = T('Enter a value')
		elif not form.vars.last_name:
			form.errors.last_name = T('Enter a value')

# employee
def employee():
	table = db.employee
	orderby = ~table.id
	onvalidation = __onvalidation_employee
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
										sortable, orderby, links, csv, showbuttontext, onvalidation, 
										oncreate, onupdate, ondelete)

# bank
def bank():
	table = db.bank
	orderby = ~table.id
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
										sortable, orderby, links, csv, showbuttontext, onvalidation, 
										oncreate, onupdate, ondelete)

# customer
def customer():
	table = db.customer
	orderby = ~table.id
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
										sortable, orderby, links, csv, showbuttontext, onvalidation, 
										oncreate, onupdate, ondelete)

# supplier
def supplier():
	table = db.supplier
	orderby = ~table.id
	return administration_master.grid_0(table, create, editable, deletable, details, searchable, 
										sortable, orderby, links, csv, showbuttontext, onvalidation, 
										oncreate, onupdate, ondelete)
