# -*- coding: utf-8 -*-

response.title = '%s - %s' %(request.controller.replace('_',' ').title(), 
							 request.function.replace('_',' ').title() )

response.logo = A(IMG(_src = URL('static', 'images/logo.png'), 
					  _width = "20px", _title = 'Administration', _alt = 'Administration'), 
				  _href = '#', _class = "navbar-brand")

response.meta.author = configuration.get('app.author')
response.meta.description = configuration.get('app.description')
response.meta.keywords = configuration.take('app.keywords')

response.google_analytics_id = configuration.get('google_analytics_id.google_analytics_id')

if auth.is_logged_in() and auth.has_membership('Admin'):
	response.menu = [
		(T('Master'), False, URL('master', 'index'), [
			(T('Customer'), False, URL('master', 'customer'), []), 
			(T('Supplier'), False, URL('master', 'supplier'), []), 
			(T('Company'), False, URL('master', 'company'), []), 
			(T('Branch'), False, URL('master', 'branch'), []), 
			(T('Department'), False, URL('master', 'department'), []), 
			(T('Role'), False, URL('master', 'role'), []), 
			(T('Employee'), False, URL('master', 'employee'), []), 
			(T('Bank'), False, URL('master', 'bank'), []), 
			(T('User'), False, URL('master', 'user'), []), 
			(T('Group'), False, URL('master', 'group'), []), 
			(T('Membership'), False, URL('master', 'membership'), []), 
			(T('Permission'), False, URL('master', 'permission'), []), 
			(T('Event'), False, URL('master', 'event'), []), 
		]), 
		(T('Administration'), False, URL('administration', 'index'), [
			(T('Acknowledgement of Work Result'), False, URL('administration', 'acknowledgement_of_work_result'), []),
			(T('Official Travel'), False, URL('administration', 'official_travel'), []),
		]), 
		(T('Report'), False, URL('report', 'index'), [
			(T('Customer'), False, URL('report', 'report_customer'), []),
			(T('Supplier'), False, URL('report', 'report_supplier'), []),
			(T('Acknowledgement of Work Result'), False, URL('report', 'report_acknowledgement_of_work_result'), []),
			(T('Official Travel'), False, URL('report', 'official_travel'), []),
		]), 
		(T('Settings'), False, URL('settings', 'index'), [
			(T('Language'), False, URL('settings', 'language'), []),
		]), 
	]
elif auth.is_logged_in():
	response.menu = [
		(T('Master'), False, URL('master', 'index'), [
			(T('Customer'), False, URL('master', 'customer'), []), 
			(T('Supplier'), False, URL('master', 'supplier'), []), 
		]), 
		(T('Administration'), False, URL('administration', 'index'), [
			(T('Acknowledgement of Work Result'), False, URL('administration', 'acknowledgement_of_work_result'), []),
			(T('Official Travel'), False, URL('administration', 'official_travel'), []),
		]), 
		(T('Report'), False, URL('report', 'index'), [
			(T('Customer'), False, URL('report', 'report_customer'), []),
			(T('Supplier'), False, URL('report', 'report_supplier'), []),
			(T('Acknowledgement of Work Result'), False, URL('report', 'report_acknowledgement_of_work_result'), []),
			(T('Official Travel'), False, URL('report', 'official_travel'), []),
		]), 
		(T('Settings'), False, URL('settings', 'index'), [
			(T('Language'), False, URL('settings', 'language'), []),
		]), 
	]

