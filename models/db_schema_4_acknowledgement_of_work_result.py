# -*- coding: utf-8 -*-

# on_define_acknowledgement_of_work_result
def on_define_acknowledgement_of_work_result(table): 
	# comment
	table.customer.comment = A(_class="glyphicon glyphicon-plus-sign", **{"_data-toggle":"modal", "_data-target":"#modal_customer"} ) if request.controller != 'report' else None
	# default
	table.acknowledgement_of_work_result_date.default = request.now
	# label
	table.acknowledgement_of_work_result_no.label = T('Acknowledgement of Work Result No')
	table.acknowledgement_of_work_result_date.label = T('Acknowledgement of Work Result Date')
	table.customer.label = T('Customer')
	table.working_on.label = T('Working On')
	table.detail_works.label = T('Detail Works')
	# notnull
	table.acknowledgement_of_work_result_no.notnull = True
	table.acknowledgement_of_work_result_date.notnull = True
	table.customer.notnull = True
	table.working_on.notnull = True
	table.detail_works.notnull = True
	# required
	table.acknowledgement_of_work_result_no.required = True
	table.acknowledgement_of_work_result_date.required = True
	table.customer.required = True
	table.working_on.required = True
	table.detail_works.required = True
	# requires
	table.customer.requires = IS_IN_DB(db, db.customer.id, db.customer._format)
	table.working_on.requires = IS_DATE(format = T('%Y-%m-%d'), error_message = T('must be YYYY-MM-DD!') )
	table.detail_works.requires = IS_NOT_EMPTY()
	# unique
	table.acknowledgement_of_work_result_no.unique = True
	# writable
	table.acknowledgement_of_work_result_no.writable = False

# create table : acknowledgement_of_work_result
db.define_table('acknowledgement_of_work_result', 
	Field('acknowledgement_of_work_result_no'),
	Field('acknowledgement_of_work_result_date', 'date'),
	Field('customer', 'reference customer'),
	Field('working_on', 'date'),
	Field('detail_works', 'list:string'),
	auth.signature, 
	on_define = on_define_acknowledgement_of_work_result, 
	format = '%(acknowledgement_of_work_result_no)s')
