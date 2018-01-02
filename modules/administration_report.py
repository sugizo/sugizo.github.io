#!/usr/bin/env python
# coding: utf8
from gluon import *

# report function : acknowledgement_of_work_result, official_travel
def report_0(table, create, editable, deletable, details, searchable, 
		     sortable, orderby, links, csv, showbuttontext):
	grid = SQLFORM.smartgrid(table, create = create, editable = editable, deletable = deletable, 
							 details = details, searchable = searchable, sortable = sortable, 
							 orderby = orderby, links = links, csv = csv, showbuttontext = showbuttontext)
	return locals()