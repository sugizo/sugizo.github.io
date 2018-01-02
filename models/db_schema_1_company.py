# -*- coding: utf-8 -*-

# on_define_company
def on_define_company(table): 
	# autodelete
	table.logo.autodelete = True
	# label
	table.name.label = T('Name')
	table.website.label = T('Website')
	table.logo.label = T('Logo')
	# notnull
	table.name.notnull = True
	# readable
	table.logo.readable = False
	# represent
	if 'company' in request.function :
		table.website.represent = lambda website, field: \
			A(website, _title = T("View Website"), _target = "_blank", _href = "%s" % website) if website else ''
	# required
	table.name.required = True
	# requires
	table.name.requires = IS_NOT_IN_DB(db, table.name)
	table.website.requires = IS_EMPTY_OR([IS_URL(), IS_NOT_IN_DB(db, table.website)])
	table.logo.requires = IS_EMPTY_OR(IS_IMAGE())
	# unique
	table.name.unique = True
	table.website.unique = True
	# uploadfolder
	table.logo.uploadfolder = os.path.join(request.folder, 'uploads', 'images', 'company', 'logo')

# create table : company
db.define_table('company', 
	Field('name'), 
	Field('website'), 
	Field('logo', 'upload'), 
	auth.signature,
	on_define = on_define_company, 
	format = '%(name)s')
