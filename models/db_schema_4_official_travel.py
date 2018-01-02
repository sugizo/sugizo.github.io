# -*- coding: utf-8 -*-

# on_define_official_travel
def on_define_official_travel(table): 
	# comment
	table.employee.comment = A(_class="glyphicon glyphicon-plus-sign", **{"_data-toggle":"modal", "_data-target":"#modal_employee"} ) if request.controller != 'report' else None
	# default
	table.official_travel_date.default = request.now
	# label
	table.official_travel_no.label = T('Official Travel No')
	table.official_travel_date.label = T('Official Travel Date')
	table.employee.label = T('Employee')
	table.date_of_depart.label = T('Date of Depart')
	table.date_of_return.label = T('Date of Return')
	table.purpose.label = T('Detail Works')
	# notnull
	table.official_travel_no.notnull = True
	table.official_travel_date.notnull = True
	table.employee.notnull = True
	table.date_of_depart.notnull = True
	table.date_of_return.notnull = True
	table.purpose.notnull = True
	# required
	table.official_travel_no.required = True
	table.official_travel_date.required = True
	table.employee.required = True
	table.date_of_depart.required = True
	table.date_of_return.required = True
	table.purpose.required = True
	# requires
	table.employee.requires = IS_IN_DB(db, db.employee.id, db.employee._format)
	table.date_of_depart.requires = IS_DATE(format = T('%Y-%m-%d'), error_message = T('must be YYYY-MM-DD!') )
	table.date_of_return.requires = IS_DATE(format = T('%Y-%m-%d'), error_message = T('must be YYYY-MM-DD!') )
	table.purpose.requires = IS_NOT_EMPTY()
	# unique
	table.official_travel_no.unique = True
	# writable
	table.official_travel_no.writable = False

# create table : official_travel
db.define_table('official_travel', 
	Field('official_travel_no'),
	Field('official_travel_date', 'date'),
	Field('employee', 'reference employee'),
	Field('date_of_depart', 'date'),
	Field('date_of_return', 'date'),
	Field('purpose', 'text'),
	auth.signature, 
	on_define = on_define_official_travel, 
	format = '%(official_travel_no)s')
