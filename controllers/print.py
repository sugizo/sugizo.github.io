# -*- coding: utf-8 -*-

import administration_print

auth.requires_login()(lambda: None)()

# index
def index():
    return locals()

# print acknowledgement_of_work_result
def acknowledgement_of_work_result():
    return administration_print.print_0(db.acknowledgement_of_work_result.id)

# print official_travel
def official_travel():
    return administration_print.print_0(db.official_travel.id)
