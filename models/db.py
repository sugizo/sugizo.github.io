# -*- coding: utf-8 -*-

# import modules needed
import os
from functools import partial

## session secure
#session.secure()

## request requires https
#request.requires_https()

from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True and change configuration.get into configuration.take to gain full speed
config_path = os.path.join(request.folder, 'private')

## once in production, set reload=False to gain full speed
configuration = AppConfig('%s/appconfig.ini' % config_path, reload = True)
configuration_env = configuration.get('environment.type')

## uncomment when running on development
from gluon.custom_import import track_changes; track_changes(True)

## Database
db = DAL(configuration.get(configuration_env + '_' + 'db.uri'), 
		 pool_size = configuration.get(configuration_env + '_' + 'db.pool_size'), 
		 migrate_enabled = configuration.get(configuration_env + '_' + 'db.migrate_enabled'), 
		 #migrate = configuration.get(configuration_env + '_' + 'db.migrate'), 
		 #fake_migrate = configuration.get(configuration_env + '_' + 'db.fake_migrate'), 
		 #fake_migrate_all = configuration.get(configuration_env + '_' + 'db.fake_migrate_all'), 
		 check_reserved = ['all'], 
		 lazy_tables = True)

response.generic_patterns = ['*'] if request.is_local else []

## choose a style for forms
response.formstyle = configuration.get('forms.formstyle')
response.form_label_separator = configuration.get('forms.separator') or ''

## (optional) optimize handling of static files
response.optimize_css = 'concat,minify,inline'
response.optimize_js = 'concat,minify,inline'

## (optional) static assets folder versioning
#response.static_version = '0.0.0'

from gluon.tools import Auth, Service, PluginManager, prettydate
auth = Auth(db, host_names = configuration.get(configuration_env + '_' + 'host.names') )
service, plugins = Service(), PluginManager()

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else configuration.get(configuration_env + '_' + 'smtp.server')
#mail.settings.server = configuration.get(configuration_env + '_' + 'smtp.server')
mail.settings.sender = configuration.get(configuration_env + '_' + 'smtp.sender')
mail.settings.login = configuration.get(configuration_env + '_' + 'smtp.login')
mail.settings.tls = configuration.get(configuration_env + '_' + 'smtp.tls') or False
mail.settings.ssl = configuration.get(configuration_env + '_' + 'smtp.ssl') or False

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
auth.settings.actions_disabled = configuration.take('auth.actions_disabled')
auth.settings.create_user_groups = False
auth.settings.everybody_group_id = configuration.get('auth.everybody_group_id')

# import custom modules
import administration_event

# for use in modules
from gluon import current
current.db = db
current.auth = auth
current.mail = mail

audit_from = db.Table(db, 'audit_from',
    Field('created_from', default = request.client, readable = False, writable = False),
    Field('modified_from', update = request.client, readable = False, writable = False) )

db._common_fields.append(audit_from)

## set the language
if 'language' in request.cookies and not (request.cookies['language'] is None):
    T.force(request.cookies['language'].value)
else:
	T.force('id')

"""
## response.models_to_run
if request.function == 'company' :
	response.models_to_run = ['db_schema_0_bank.py', 'db_schema_0_company.py', 'db_schema_0_department.py', 
							  'db_schema_1_branch.py', 'menu.py']
elif request.function == 'bank' :
	response.models_to_run = ['db_schema_0_bank.py', 'db_schema_0_company.py', 'db_schema_0_department.py', 
							  'db_schema_1_branch.py', 'menu.py']
elif request.function == 'department' :
	response.models_to_run = ['db_schema_0_bank.py', 'db_schema_0_company.py', 'db_schema_0_department.py', 
							  'db_schema_1_branch.py', 'menu.py']
elif request.function == 'branch' :
	response.models_to_run = ['db_schema_0_bank.py', 'db_schema_0_company.py', 'db_schema_0_department.py', 
							  'db_schema_1_branch.py', 'menu.py']
elif request.function == 'customer' :
	response.models_to_run = ['db_schema_0_bank.py', 'db_schema_0_company.py', 'db_schema_0_department.py', 
							  'db_schema_1_branch.py', 'db_schema_2_customer.py', 'menu.py']
elif request.function == 'supplier' :
	response.models_to_run = ['db_schema_0_bank.py', 'db_schema_0_company.py', 'db_schema_0_department.py', 
							  'db_schema_1_branch.py', 'db_schema_2_supplier.py', 'menu.py']
elif request.function == 'acknowledgement_of_work_result' :
	response.models_to_run = ['db_schema_0_bank.py', 'db_schema_0_company.py', 'db_schema_0_department.py', 
							  'db_schema_1_branch.py', 'db_schema_2_customer.py', 
							  'db_schema_3_acknowledgement_of_work_result.py', 'menu.py']
elif request.function == 'report_customer' :
	response.models_to_run = ['db_schema_0_bank.py', 'db_schema_0_company.py', 'db_schema_0_department.py', 
							  'db_schema_1_branch.py', 'db_schema_2_customer.py', 
							  'db_schema_3_acknowledgement_of_work_result.py', 'menu.py']
elif request.function == 'report_supplier' :
	response.models_to_run = ['db_schema_0_bank.py', 'db_schema_0_company.py', 'db_schema_0_department.py', 
							  'db_schema_1_branch.py', 'db_schema_2_supplier.py', 
							  'menu.py']
elif request.function == 'report_acknowledgement_of_work_result' :
	response.models_to_run = ['db_schema_0_bank.py', 'db_schema_0_company.py', 'db_schema_0_department.py', 
							  'db_schema_1_branch.py', 'db_schema_2_customer.py', 
							  'db_schema_3_acknowledgement_of_work_result.py', 'menu.py']
else:
	response.models_to_run = ['.*']
"""
