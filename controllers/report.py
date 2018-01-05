# -*- coding: utf-8 -*-

import administration_report

auth.requires_login()(lambda: None)()

create = False
editable = has_membership_admin
deletable = False
details = True
searchable = True
sortable = True
links = None
csv = True
showbuttontext = False

# index
def index():
    return locals()

# report_customer
def report_customer():
	table = db.customer
	orderby = dict(customer = ~table.id)
	return administration_report.report_0(table, create, editable, deletable, details, searchable, 
										  sortable, orderby, links, csv, showbuttontext)

# report_supplier
def report_supplier():
	table = db.supplier
	orderby = dict(supplier = ~table.id)
	return administration_report.report_0(table, create, editable, deletable, details, searchable, 
										  sortable, orderby, links, csv, showbuttontext)

# report_acknowledgement_of_work_result
def report_acknowledgement_of_work_result():
	table = db.acknowledgement_of_work_result
	orderby = dict(acknowledgement_of_work_result = ~table.id)
	links = [dict(header = T('Action'), 
				  body = lambda row: DIV(A(I(_class = 'glyphicon glyphicon-print'), 
										   _title = T("Print"), 
										   _target = "_blank", _class = "button", 
										   _href = URL("print", "acknowledgement_of_work_result", 
										   args = [row.id]) ), 
										 A(I(_class = 'glyphicon glyphicon-envelope'), 
										   _title = T("Mail"), 
										   _target = "_blank", _class = "button", 
										   _href = "mailto:%s?subject=%s&body=%s" 
										   % (", ".join(mail for mail in row.customer.email), 
										   'Acknowledgement of Work Result', 
										   response.render('report/mail_acknowledgement_of_work_result.html', 
										   dict(header_id=row.id) ) ) )
										)
				 )
			]
	return administration_report.report_0(table, create, editable, deletable, details, searchable, 
										  sortable, orderby, links, csv, showbuttontext)

# report_official_travel
def report_official_travel():
	table = db.official_travel
	orderby = dict(official_travel = ~table.id)
	links = [dict(header = T('Action'), 
				  body = lambda row: DIV(A(I(_class = 'glyphicon glyphicon-print'), 
										   _title = T("Print"), 
										   _target = "_blank", _class = "button", 
										   _href = URL("print", "official_travel", 
										   args = [row.id]) ), 
										 A(I(_class = 'glyphicon glyphicon-envelope'), 
										   _title = T("Mail"), 
										   _target = "_blank", _class="button", 
										   _href = "mailto:%s?subject=%s&body=%s" 
										   % (", ".join(mail for mail in row.employee.email), 
										   'Acknowledgement of Work Result', 
										   response.render('report/mail_official_travel.html', 
										   dict(header_id=row.id) ) ) )
										)
				 )
			]
	return administration_report.report_0(table, create, editable, deletable, details, searchable, 
										  sortable, orderby, links, csv, showbuttontext)
