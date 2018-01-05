# -*- coding: utf-8 -*-

# on_define_employee
def on_define_employee(table): 
	# comment
	table.auth_user.comment = A(_class="glyphicon glyphicon-plus-sign", **{"_data-toggle":"modal", "_data-target":"#modal_auth_user"} ) if request.controller != 'report' else None
	table.bank.comment = A(_class="glyphicon glyphicon-plus-sign", **{"_data-toggle":"modal", "_data-target":"#modal_bank"} ) if request.controller != 'report' else None
	table.branch.comment = A(_class="glyphicon glyphicon-plus-sign", **{"_data-toggle":"modal", "_data-target":"#modal_branch"} ) if request.controller != 'report' else None
	table.department.comment = A(_class="glyphicon glyphicon-plus-sign", **{"_data-toggle":"modal", "_data-target":"#modal_department"} ) if request.controller != 'report' else None
	table.role.comment = A(_class="glyphicon glyphicon-plus-sign", **{"_data-toggle":"modal", "_data-target":"#modal_role"} ) if request.controller != 'report' else None
	# default
	table.is_auth.default = False
	# label
	table.is_auth.label = T('Is Auth?')
	table.auth_user.label = T('Auth User')
	table.username.label = T('Username')
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
	table.ym.label = T('Yahoo Messenger')
	table.bank.label = T('Bank')
	table.account_no.label = T('Account No')
	table.branch.label = T('Branch')
	table.department.label = T('Department')
	table.role.label = T('Role')
	table.notes.label = T('Notes')
	# notnull
	table.salutation.notnull = True
	table.first_name.notnull = True
	table.last_name.notnull = True
	table.gender.notnull = True
	table.bank.notnull = True
	table.account_no.notnull = True
	table.branch.notnull = True
	table.department.notnull = True
	table.role.notnull = True
	# represent
	if 'employee' in request.function :
		table.address.represent = lambda address, field: \
			A(address, _title=T("View Maps"), _target="_blank", 
			  _href="http://maps.google.com/maps?f=q&hl=en&geocode=&time=&date=&ttype=&q=%s,+%s,+%s" 
			  % (field.address, field.city, field.country) ) if address else ''
		table.email.represent = lambda email, field: \
			XML(", ".join([A(mail, _title=T("Send to %s") % mail, _target="_blank", 
							 _href="mailto:%s" % mail).xml() for mail in email] ) ) if email else ''
		table.ym.represent = lambda ym, field: \
			XML(", ".join([A(IMG(_title=T("Chat with %s") % yahoo, _alt=T("Chat with %s") % yahoo, 
			_src="http://www.imvisible.info/status-image.php?id=%s&icon=1" % yahoo), 
			_target="_blank", _href="ymsgr:sendIM?%s" % yahoo).xml() for yahoo in ym]) ) if ym else ''
		table.bank.represent = lambda bank, field: \
			A(bank.name, _title=T("website"), _target="_blank", _href="%s" % bank.website)
		table.branch.represent = lambda branch, field: \
			A(branch.address, _title=T("View Maps"), _target="_blank", 
			  _href="http://maps.google.com/maps?f=q&hl=en&geocode=&time=&date=&ttype=&q=%s,+%s,+%s" % (field.branch.address, field.branch.city, field.branch.country) )
	# required
	table.salutation.required = True
	table.first_name.required = True
	table.last_name.required = True
	table.gender.required = True
	table.bank.required = True
	table.account_no.required = True
	table.branch.required = True
	table.department.required = True
	table.role.required = True
	# requires
	table.auth_user.requires = IS_EMPTY_OR(IS_IN_DB(db, db.auth_user.id, db.auth_user._format) )
	table.salutation.requires = IS_IN_SET([('Mr.', T('Mr.') ), ('Mrs.', T('Mrs.') ), ('Ms.', T('Ms.') ) ] )
	table.gender.requires = IS_IN_SET([('Male', T('Male') ), ('Female', T('Female') ) ] )
	table.zip_code.requires = IS_EMPTY_OR(IS_MATCH('^\d{5,5}$', error_message = T('not a Zip Code') ) )
	table.email.requires = IS_LIST_OF([IS_LOWER(), IS_EMAIL(), IS_NOT_IN_DB(db, table.email) ] )
	table.bank.requires = IS_IN_DB(db, db.bank.id, db.bank._format)
	table.account_no.requires = IS_NOT_EMPTY()
	table.branch.requires = IS_IN_DB(db, db.branch.id, db.branch._format)
	table.department.requires = IS_IN_DB(db, db.department.id, db.department._format)
	table.role.requires = IS_IN_DB(db, db.role.id, db.role._format)
	# show_if
	table.auth_user.show_if = (table.is_auth == True)
	table.first_name.show_if = (table.is_auth == False)
	table.last_name.show_if = (table.is_auth == False)
	table.email.show_if = (table.is_auth == False)
	# unique
	table.username.unique = True
	table.email.unique = True

# create table : employee
db.define_table('employee', 
	Field('is_auth', 'boolean'),
	Field('auth_user', 'reference auth_user'), 
	Field('username'), 
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
	Field('ym', 'list:string'), 
	Field('bank', 'reference bank'), 
	Field('account_no'), 
	Field('branch', 'reference branch'), 
	Field('department', 'reference department'), 
	Field('role', 'reference role'), 
	Field('notes', 'text'), 
	auth.signature,
	on_define = on_define_employee, 
	format = lambda r: '%s - %s' % (r.first_name, r.last_name) )
