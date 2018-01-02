# -*- coding: utf-8 -*-

# on_define_bank
def on_define_bank(table): 
	# label
	table.name.label = T('Name')
	table.ebanking.label = T('eBanking')
	# notnull
	table.name.notnull = True
	# represent
	if 'bank' in request.function :
		table.ebanking.represent = lambda ebanking, field: \
			A(ebanking, _title=T("eBanking"), _target="_blank", _href="%s" % ebanking) if ebanking else ''
	# required
	table.name.required = True
	# requires
	table.name.requires = IS_NOT_IN_DB(db, table.name)
	# unique
	table.name.unique = True

# create table : bank
db.define_table('bank', 
	Field('name'), 
	Field('ebanking'), 
	auth.signature,
	on_define = on_define_bank, 
	format = '%(name)s')
