# -*- coding: utf-8 -*-

# on_define_department
def on_define_department(table): 
	# label
	table.name.label = T('Name')
	# notnull
	table.name.notnull = True
	# required
	table.name.required = True
	# requires
	table.name.requires = IS_NOT_IN_DB(db, table.name)
	# unique
	table.name.unique = True

# create table : department
db.define_table('department', 
	Field('name'), 
	auth.signature,
	on_define = on_define_department, 
	format = '%(name)s')
