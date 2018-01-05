#!/usr/bin/env python
# coding: utf8
from gluon import *

# oncreate_event
def oncreate_event(form, table):
	current.db.auth_event.insert(time_stamp = current.request.now, 
								 client_ip = current.request.client, 
								 user_id = current.auth.user_id, 
								 origin = '%s/%s' % (current.request.controller, 
													 current.request.function), 
								 description = 'ID %s created in table %s' % (form.vars.id, table) )

# onupdate_event
def onupdate_event(form, table):
	if form.vars.delete_this_record:
		current.db.auth_event.insert(time_stamp = current.request.now, 
									 client_ip = current.request.client, 
									 user_id = current.auth.user_id, 
									 origin = '%s/%s' % (current.request.controller, 
														 current.request.function), 
									 description = 'ID %s deleted in table %s' % (form.vars.id, table) )
	else:
		current.db.auth_event.insert(time_stamp = current.request.now, 
									 client_ip = current.request.client, 
									 user_id = current.auth.user_id, 
									 origin = '%s/%s' % (current.request.controller, 
														 current.request.function), 
									 description = 'ID %s updated in table %s' % (form.vars.id, table) )

# ondelete_event
def ondelete_event(table, id):
	current.db.auth_event.insert(time_stamp = current.request.now, 
								 client_ip = current.request.client, 
								 user_id = current.auth.user_id, 
								 origin = '%s/%s' % (current.request.controller, 
													 current.request.function), 
								 description = 'ID %s deleted in table %s' % (id, table) )

# onfail_event
def onfail_event(id, username):
	current.db.auth_event.insert(time_stamp = current.request.now, 
								 client_ip = current.request.client, 
								 user_id = id, 
								 origin = '%s/%s' % (current.request.controller, 
													 current.request.function), 
								 description = '%s login failed' % (username) )

# onexecute_event
def onexecute_event():
	current.db.auth_event.insert(time_stamp = current.request.now, 
								 client_ip = current.request.client, 
								 user_id = current.auth.user_id, 
								 origin = '%s/%s' % (current.request.controller, 
													 current.request.function), 
								 description = 'Command executed' )

# after_insert_event
def after_insert_event(f, id, table):
	current.db.auth_event.insert(time_stamp = current.request.now, 
								 client_ip = current.request.client, 
								 user_id = current.auth.user_id, 
								 origin = '%s/%s' % (current.request.controller, 
													 current.request.function), 
								 description = 'ID %s created in table %s' % (id, table) )

# after_update_event
def after_update_event(s, f, table):
	if not ('is_active' in f and f['is_active'] == False) and '_archive' not in table:
		table_input = s.select().first()
		current.db.auth_event.insert(time_stamp = current.request.now, 
									 client_ip = current.request.client, 
									 user_id = current.auth.user_id, 
									 origin = '%s/%s' % (current.request.controller, 
														 current.request.function), 
									 description='ID %s updated in table %s' % (table_input.id, table) )

# before_delete_event
def before_delete_event(s, table):
	table_input = s.select().first()
	if table_input and '_archive' not in table:
		current.db.auth_event.insert(time_stamp = current.request.now, 
									 client_ip = current.request.client, 
									 user_id = current.auth.user_id, 
									 origin = '%s/%s' % (current.request.controller, 
														 current.request.function), 
									 description='ID %s deleted in table %s' % (table_input.id, table) )
