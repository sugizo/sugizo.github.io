# -*- coding: utf-8 -*-

# create all tables needed by auth if not custom tables
auth.define_tables(username = True, signature = True)

""" custom_auth_table """
custom_auth_table = db[auth.settings.table_user_name]

# format
custom_auth_table._format = '%(first_name)s %(last_name)s'
# label
custom_auth_table.first_name.label = T('First Name')
custom_auth_table.last_name.label = T('Last Name')
custom_auth_table.email.label = T('Email')

auth.settings.table_user = custom_auth_table

# has membership manager
has_membership_admin = auth.has_membership('Manager')

# login onfail
def login_onfail(form):
	username = request.vars.username
	row = db((db.auth_user.username == username ) ).select().first()
	if row is not None:
		administration_event.onfail_event(row.id, row.username)

auth.settings.login_onfail.append(login_onfail)
