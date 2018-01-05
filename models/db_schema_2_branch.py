# -*- coding: utf-8 -*-

# on_define_branch
def on_define_branch(table): 
	# comment
	table.bank.comment = A(_class="glyphicon glyphicon-plus-sign", **{"_data-toggle":"modal", "_data-target":"#modal_bank"} ) if request.controller != 'report' else None
	table.company.comment = A(_class="glyphicon glyphicon-plus-sign", **{"_data-toggle":"modal", "_data-target":"#modal_company"} ) if request.controller != 'report' else None
	# label
	table.address.label = T('Address')
	table.zip_code.label = T('Zip Code')
	table.city.label = T('City')
	table.country.label = T('Country')
	table.phone.label = T('Phone')
	table.fax.label = T('Fax')
	table.email.label = T('Email')
	table.bank.label = T('Bank')
	table.company.label = T('Company')
	# notnull
	table.address.notnull = True
	table.zip_code.notnull = True
	table.city.notnull = True
	table.country.notnull = True
	table.phone.notnull = True
	table.email.notnull = True
	table.bank.notnull = True
	table.company.notnull = True
	# represent
	if 'branch' in request.function :
		table.address.represent = lambda address, field: \
			A(address, _title=T("View Maps"), _target="_blank", _href="http://maps.google.com/maps?f=q&hl=en&geocode=&time=&date=&ttype=&q=%s,+%s,+%s" % (field.address, field.city, field.country))
		table.email.represent = lambda email, field: \
			XML(", ".join([A(mail, _title=T("Send to %s") % mail, _target="_blank", _href="mailto:%s" % mail).xml() for mail in email]))
		table.bank.represent = lambda bank, field: \
			XML(", ".join([A(bank.name, _title=T("eBanking"), _target="_blank", _href="%s" % bank.ebanking).xml() for bank in field.bank]))
		table.company.represent = lambda company, field: \
			A(field.company.name, _title=T("View Website"), _target="_blank", _href="%s" % field.company.website)
	# required
	table.address.required = True
	table.zip_code.required = True
	table.city.required = True
	table.country.required = True
	table.phone.required = True
	table.email.required = True
	table.bank.required = True
	table.company.required = True
	# requires
	table.address.requires = IS_NOT_IN_DB(db, table.address)
	table.zip_code.requires = IS_MATCH('^\d{5,5}$', error_message = 'not a Zip Code')
	table.city.requires=IS_NOT_EMPTY()
	table.country.requires=IS_NOT_EMPTY()
	table.phone.requires = IS_NOT_IN_DB(db, table.phone)
	table.fax.requires = IS_EMPTY_OR(IS_NOT_IN_DB(db, table.fax))
	table.email.requires = IS_LIST_OF([IS_LOWER(), IS_EMAIL(), IS_NOT_IN_DB(db, table.email) ] )
	table.bank.requires = IS_IN_DB(db, db.bank.id, db.bank._format)
	table.company.requires = IS_IN_DB(db, db.company.id, db.company._format)
	# unique
	table.address.unique = True
	table.phone.unique = True
	table.fax.unique = True
	table.email.unique = True
	
# create table : branch
db.define_table('branch', 
	Field('address', 'text'), 
	Field('zip_code'), 
	Field('city'), 
	Field('country'), 
	Field('phone', 'list:string'), 
	Field('fax', 'list:string'), 
	Field('email', 'list:string'), 
	Field('bank', 'list:reference bank'), 
	Field('company', 'reference company'), 
	auth.signature,
	on_define = on_define_branch, 
	format = '%(address)s')
