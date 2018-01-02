# -*- coding: utf-8 -*-

import administration_administration

auth.requires_login()(lambda: None)()

# index
def index():
    return locals()

""" modal """
# modal_customer
def modal_customer():
	table = db.customer
	fields = None
	target_response = '(function($) {$("#modal_customer").modal("hide");}(jQuery));'
	return administration_administration.form_0(table, fields, target_response)

# modal_employee
def modal_employee():
	table = db.employee
	fields = None
	target_response = '(function($) {$("#modal_employee").modal("hide");}(jQuery));'
	return administration_administration.form_0(table, fields, target_response)

""" acknowledgement_of_work_result """
# onvalidation_acknowledgement_of_work_result
def __onvalidation_acknowledgement_of_work_result(form):
	id_max_acknowledgement_of_work_result = db.acknowledgement_of_work_result.id.max()
	maxID_acknowledgement_of_work_result = db(db.acknowledgement_of_work_result).select(id_max_acknowledgement_of_work_result).first()[id_max_acknowledgement_of_work_result]
	acknowledgement_of_work_result_no_id = int(maxID_acknowledgement_of_work_result) + 1 if maxID_acknowledgement_of_work_result else 1
	customer_for_acknowledgement_of_work_result_no = str(request.vars.customer)
	acknowledgement_of_work_result_no = customer_for_acknowledgement_of_work_result_no+'/AOWR/'+request.now.strftime('%y%m%d')+'/'+str(acknowledgement_of_work_result_no_id)
	
	form.vars.acknowledgement_of_work_result_no = acknowledgement_of_work_result_no

# acknowledgement_of_work_result
def acknowledgement_of_work_result():
	table = db.acknowledgement_of_work_result
	fields = ['customer', 'working_on', 'detail_works']
	onvalidation = __onvalidation_acknowledgement_of_work_result
	report = 'report_acknowledgement_of_work_result'
	return administration_administration.form_1(table, fields, onvalidation, report)

""" official_travel """
# onvalidation_official_travel
def __onvalidation_official_travel(form):
	id_max_official_travel = db.official_travel.id.max()
	maxID_official_travel = db(db.official_travel).select(id_max_official_travel).first()[id_max_official_travel]
	official_travel_no_id = int(maxID_official_travel) + 1 if maxID_official_travel else 1
	employee_for_official_travel_no = str(request.vars.employee)
	official_travel_no = employee_for_official_travel_no+'/AOWR/'+request.now.strftime('%y%m%d')+'/'+str(official_travel_no_id)
	
	form.vars.official_travel_no = official_travel_no

# official_travel
def official_travel():
	table = db.official_travel
	fields = ['employee', 'date_of_depart', 'date_of_return', 'purpose']
	onvalidation = __onvalidation_official_travel
	report = 'report_official_travel'
	return administration_administration.form_1(table, fields, onvalidation, report)
