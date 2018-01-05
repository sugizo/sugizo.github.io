# -*- coding: utf-8 -*-

# on_define_supplier
def on_define_supplier(table): 
	# comment
	table.bank.comment = A(_class="glyphicon glyphicon-plus-sign", **{"_data-toggle":"modal", "_data-target":"#modal_bank"} ) if request.controller != 'report' else None
	# label
	table.salutation.label = T('Salutation')
	table.first_name.label = T('First Name')
	table.last_name.label = T('Last Name')
	table.gender.label = T('Gender')
	table.address.label = T('Address')
	table.zip_code.label = T('Zip Code')
	table.city.label = T('City')
	table.country.label = T('Country')
	table.phone.label = T('Phone')
	table.email.label = T('Email')
	table.bank.label = T('Bank')
	table.account_no.label = T('Account No.')
	table.notes.label = T('Notes')
	# notnull
	table.salutation.notnull = True
	table.first_name.notnull = True
	table.gender.notnull = True
	table.bank.notnull = True
	# represent
	if 'supplier' in request.function :
		table.address.represent = lambda address, field: \
			A(address, _title=T("View Maps"), _target="_blank", 
			  _href="http://maps.google.com/maps?f=q&hl=en&geocode=&time=&date=&ttype=&q=%s,+%s,+%s" 
			  % (field.address, field.city, field.country) ) if address else ''
		table.email.represent = lambda email, field: \
			XML(", ".join([A(mail, _title=T("Send to %s") % mail, _target="_blank", 
							 _href="mailto:%s" % mail).xml() for mail in email] ) ) if email else ''
		table.bank.represent = lambda bank, field: \
			A(bank.name, _title=T("eBanking"), _target="_blank", _href="%s" % bank.ebanking)
	# required
	table.salutation.required = True
	table.first_name.required = True
	table.gender.required = True
	table.bank.required = True
	# requires
	table.salutation.requires = IS_IN_SET([('Mr.', T('Mr.') ), ('Mrs.', T('Mrs.') ), ('Ms.', T('Ms.') ) ] )
	table.first_name.requires = IS_NOT_EMPTY()
	table.gender.requires = IS_IN_SET([('Male', T('Male') ), ('Female', T('Female') ) ] )
	table.zip_code.requires = IS_EMPTY_OR(IS_MATCH('^\d{5,5}$', error_message = T('not a Zip Code') ) )
	table.email.requires = IS_LIST_OF([IS_LOWER(), IS_EMAIL(), IS_NOT_IN_DB(db, table.email) ] )
	table.bank.requires = IS_IN_DB(db, db.bank.id, db.bank._format)
	# unique
	table.email.unique = True

# create table : supplier
db.define_table('supplier', 
	Field('salutation'), 
	Field('first_name'), 
	Field('last_name'), 
	Field('gender'), 
	Field('address', 'text'), 
	Field('zip_code'), 
	Field('city'), 
	Field('country'), 
	Field('phone', 'list:string'), 
	Field('email', 'list:string'), 
	Field('bank', 'reference bank'), 
	Field('account_no'), 
	Field('notes', 'text'), 
	auth.signature, 
	on_define = on_define_supplier, 
	format = lambda r: '%s - %s' % (r.first_name, r.last_name) )
