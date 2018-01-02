# -*- coding: utf-8 -*-

# on_define_role
def on_define_role(table): 
	# label
	table.code.label = T('Code')
	table.name.label = T('Name')
	# notnull
	table.code.notnull = True
	table.name.notnull = True
	# required
	table.code.required = True
	table.name.required = True
	# requires
	table.code.requires = IS_NOT_IN_DB(db, table.code)
	table.name.requires = IS_NOT_IN_DB(db, table.name)
	# unique
	table.code.unique = True
	table.name.unique = True

# create table : role
db.define_table('role', 
	Field('code'), 
	Field('name'),
	auth.signature,
	on_define = on_define_role, 
	format = '%(name)s')
