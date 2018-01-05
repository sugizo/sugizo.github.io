# -*- coding: utf-8 -*-

# index
def index():
	if db(db.auth_permission).isempty() and db(db.auth_membership).isempty():
		""" insert """
		# group
		auth.add_group('Admin', 'Admin')
		auth.add_group('Manager', 'Manager')
		auth.add_group('Staff', 'Staff')
		auth.add_group('Accounting', 'Accounting')
		auth.add_group('Finance', 'Finance')
		auth.add_group('HR', 'HR')
		auth.add_group('IT', 'IT')
		auth.add_group('Purchase', 'Purchase')
		auth.add_group('Sale', 'Sale')
		auth.add_group('Service', 'Service')
		auth.add_group('Warehouse', 'Warehouse')
		
		# user
		db.auth_user.bulk_insert([{"first_name" : "Admin", "last_name" : "Admin", 
								   "email" : "admin@stifix.com", "username" : "admin", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Accounting", "last_name" : "Manager", 
								   "email" : "accountingmanager@stifix.com", "username" : "accountingmanager", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Finance", "last_name" : "Manager", 
								   "email" : "financemanager@stifix.com", "username" : "financemanager", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "HR", "last_name" : "Manager", 
								   "email" : "hrmanager@stifix.com", "username" : "hrmanager", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "IT", "last_name" : "Manager", 
								   "email" : "itmanager@stifix.com", "username" : "itmanager", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Purchase", "last_name" : "Manager", 
								   "email" : "purchasemanager@stifix.com", "username" : "purchasemanager", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Sale", "last_name" : "Manager", 
								   "email" : "salemanager@stifix.com", "username" : "salemanager", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Service", "last_name" : "Manager", 
								   "email" : "servicemanager@stifix.com", "username" : "servicemanager", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Warehouse", "last_name" : "Manager", 
								   "email" : "warehousemanager@stifix.com", "username" : "warehousemanager", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Accounting", "last_name" : "Staff", 
								   "email" : "accountingstaff@stifix.com", "username" : "accountingstaff", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Finance", "last_name" : "Staff", 
								   "email" : "financestaff@stifix.com", "username" : "financestaff", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "HR", "last_name" : "Staff", 
								   "email" : "hrstaff@stifix.com", "username" : "hrstaff", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "IT", "last_name" : "Staff", 
								   "email" : "itstaff@stifix.com", "username" : "itstaff", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Purchase", "last_name" : "Staff", 
								   "email" : "purchasestaff@stifix.com", "username" : "purchasestaff", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Sale", "last_name" : "Staff", 
								   "email" : "salestaff@stifix.com", "username" : "salestaff", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Service", "last_name" : "Staff", 
								   "email" : "servicestaff@stifix.com", "username" : "servicestaff", 
								   "password" : db.auth_user.password.validate("password")[0]}, 
								  {"first_name" : "Warehouse", "last_name" : "Staff", 
								   "email" : "warehousestaff@stifix.com", "username" : "warehousestaff", 
								   "password" : db.auth_user.password.validate("password")[0]}, ])
		
		"""
		membership (group_id, user_id)
		
		Group :
		1 : Admin
		2 : Manager
		3 : Staff
		4 : Accounting
		5 : Finance
		6 : HR
		7 : IT
		8 : Purchase
		9 : Sale
		10 : Service
		11 : Warehouse
		
		User :
		1 : admin
		2 : accountingmanager
		3 : financemanager
		4 : hrmanager
		5 : itmanager
		6 : purchasemanager
		7 : salemanager
		8 : servicemanager
		9 : warehousemanager
		10 : accountingstaff
		11 : financestaff
		12 : hrstaff
		13 : itstaff
		14 : purchasestaff
		15 : salestaff
		16 : servicestaff
		17 : warehousestaff
		"""
		# Admin
		auth.add_membership('1', '1')
		auth.add_membership('2', '1')
		auth.add_membership('3', '1')
		auth.add_membership('4', '1')
		auth.add_membership('5', '1')
		auth.add_membership('6', '1')
		auth.add_membership('7', '1')
		auth.add_membership('8', '1')
		auth.add_membership('9', '1')
		auth.add_membership('10', '1')
		auth.add_membership('11', '1')
		# Accounting Manager
		auth.add_membership('2', '2')
		auth.add_membership('4', '2')
		# Finance Manager
		auth.add_membership('2', '3')
		auth.add_membership('5', '3')
		# HR Manager
		auth.add_membership('2', '4')
		auth.add_membership('6', '4')
		# IT Manager
		auth.add_membership('2', '5')
		auth.add_membership('7', '5')
		# Purchase Manager
		auth.add_membership('2', '6')
		auth.add_membership('8', '6')
		# Sale Manager
		auth.add_membership('2', '7')
		auth.add_membership('9', '7')
		# Service Manager
		auth.add_membership('2', '8')
		auth.add_membership('10', '8')
		# Warehouse Manager
		auth.add_membership('2', '9')
		auth.add_membership('11', '9')
		# Accounting Staff
		auth.add_membership('4', '10')
		# Finance Staff
		auth.add_membership('5', '11')
		# HR Staff
		auth.add_membership('6', '12')
		# IT Staff
		auth.add_membership('7', '13')
		# Purchase Staff
		auth.add_membership('8', '14')
		# Sale Staff
		auth.add_membership('9', '15')
		# Service Staff
		auth.add_membership('10', '16')
		# Warehouse Staff
		auth.add_membership('11', '17')

		# permission
		auth.add_permission(1, 'impersonate', 'auth_user', 2)
		auth.add_permission(1, 'impersonate', 'auth_user', 3)
		auth.add_permission(1, 'impersonate', 'auth_user', 4)
		auth.add_permission(1, 'impersonate', 'auth_user', 5)
		auth.add_permission(1, 'impersonate', 'auth_user', 6)
		auth.add_permission(1, 'impersonate', 'auth_user', 7)
		auth.add_permission(1, 'impersonate', 'auth_user', 8)
		auth.add_permission(1, 'impersonate', 'auth_user', 9)
		auth.add_permission(1, 'impersonate', 'auth_user', 10)
		auth.add_permission(1, 'impersonate', 'auth_user', 11)
		auth.add_permission(1, 'impersonate', 'auth_user', 12)
		auth.add_permission(1, 'impersonate', 'auth_user', 13)
		auth.add_permission(1, 'impersonate', 'auth_user', 14)
		auth.add_permission(1, 'impersonate', 'auth_user', 15)
		auth.add_permission(1, 'impersonate', 'auth_user', 16)
		auth.add_permission(1, 'impersonate', 'auth_user', 17)

		""" insert 0 """
		# bank
		db.bank.bulk_insert([{'name' : 'BCA', 'ebanking' : 'http://www.klikbca.com'}, 
							 {'name' : 'Danamon', 'ebanking' : 'https://www.danamonline.com/'}, ])

		# company
		db.company.insert(name = 'stifix', website = 'http://stifix.com')

		# department
		db.department.bulk_insert([{'name' : 'Accounting'}, 
								   {'name' : 'Finance'}, 
								   {'name' : 'HR'}, 
								   {'name' : 'IT'}, 
								   {'name' : 'Purchase'}, 
								   {'name' : 'Sale'}, 
								   {'name' : 'Service'}, 
								   {'name' : 'Warehouse'}, ])

		# role
		db.role.bulk_insert([{"code" : "code0", "name" : "Staff"}, 
						     {"code" : "code1", "name" : "Manager"}, 
						     {"code" : "code1", "name" : "Director"}, ])

		""" insert 1 """
		# branch
		db.branch.bulk_insert([{'address' : 'Jalan Kacang Polong 3, Rawa Buaya', 
								'zip_code' : '11111', 'city' : 'Jakarta', 'country' : 'Indonesia', 
								'phone' : ['1', '2'], 'fax' : ['1', '2'], 
								'email' : ['branch1@gmail.com','branch1@stifix.com'], 
								'bank' : [1, 2], 'company' : 1}, 
							   {'address' : 'Jalan Jalur Sutera, Serpong', 
								'zip_code' : '11111', 'city' : 'Banten', 'country' : 'Indonesia', 
								'phone' : ['1', '2'], 'fax' : ['1', '2'], 
								'email' : ['branch2@gmail.com','branch2@stifix.com'], 
								'bank' : [1, 2], 'company' : 1}, 
							   {'address' : 'Jalan Jenderal Sudirman, Bendungan Hilir', 
								'zip_code' : '11111', 'city' : 'Jakarta', 'country' : 'Indonesia', 
								'phone' : ['1', '2'], 'fax' : ['1', '2'], 
								'email' : ['branch3@gmail.com','branch3@stifix.com'], 
								'bank' : [1, 2], 'company' : 1}, ])

		# customer
		db.customer.bulk_insert([{'salutation' : 'Mr.', 'first_name' : 'customer', 'last_name' : 'one', 
								  'gender' : 'Male', 'address' : 'Address', 'zip_code' : '11111',  
								  'city' : 'Jakarta', 'country' : 'Indonesia', 'phone' : ['1', '2'], 
								  'email' : ['customerone@stifix.com','customertwo@stifix.com'], 'bank' : 1, 
								  'account_no' : '111', 'notes' : 'great'}, 
								 {'salutation' : 'Mr.', 'first_name' : 'customer', 'last_name' : 'two', 
								  'gender' : 'Male', 'address' : 'Address', 'zip_code' : '11111',  
								  'city' : 'Jakarta', 'country' : 'Indonesia', 'phone' : ['3', '4'], 
								  'email' : ['customerthree@stifix.com','customerfour@stifix.com'], 'bank' : 2, 
								  'account_no' : '111', 'notes' : 'great'}, ])
		
		# supplier
		db.supplier.bulk_insert([{'salutation' : 'Mr.', 'first_name' : 'supplier', 'last_name' : 'one', 
								  'gender' : 'Male', 'address' : 'Address', 'zip_code' : '11111',  
								  'city' : 'Jakarta', 'country' : 'Indonesia', 'phone' : ['1', '2'], 
								  'email' : ['supplierone@stifix.com','suppliertwo@stifix.com'], 'bank' : 1, 
								  'account_no' : '111', 'notes' : 'great'}, 
								 {'salutation' : 'Mr.', 'first_name' : 'supplier', 'last_name' : 'two', 
								  'gender' : 'Male', 'address' : 'Address', 'zip_code' : '11111',  
								  'city' : 'Jakarta', 'country' : 'Indonesia', 'phone' : ['3', '4'], 
								  'email' : ['supplierthree@stifix.com','supplierfour@stifix.com'], 'bank' : 2, 
								  'account_no' : '111', 'notes' : 'great'}, ])

		""" insert 2 """
		# employee
		db.employee.bulk_insert([{'is_auth' : 1, 'auth_user' : 1, 'username' : 'admin', 'salutation' : 'Mr.', 
								  'first_name' : 'Admin', 'last_name' : 'Admin', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['1', '2'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 4, 
								  'role' : 2, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 2, 'username' : 'accountingmanager', 'salutation' : 'Mr.', 
								  'first_name' : 'Accounting', 'last_name' : 'Manager', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 1, 
								  'role' : 2, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 3, 'username' : 'financemanager', 'salutation' : 'Mr.', 
								  'first_name' : 'Finance', 'last_name' : 'Manager', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 2, 
								  'role' : 2, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 4, 'username' : 'hrmanager', 'salutation' : 'Mr.', 
								  'first_name' : 'HR', 'last_name' : 'Manager', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 3, 
								  'role' : 2, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 5, 'username' : 'itmanager', 'salutation' : 'Mr.', 
								  'first_name' : 'IT', 'last_name' : 'Manager', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 4, 
								  'role' : 2, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 6, 'username' : 'purchasemanager', 'salutation' : 'Mr.', 
								  'first_name' : 'Purchase', 'last_name' : 'Manager', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 5, 
								  'role' : 2, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 7, 'username' : 'salemanager', 'salutation' : 'Mr.', 
								  'first_name' : 'Sale', 'last_name' : 'Manager', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 6, 
								  'role' : 2, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 8, 'username' : 'servicemanager', 'salutation' : 'Mr.', 
								  'first_name' : 'Service', 'last_name' : 'Manager', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 7, 
								  'role' : 2, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 9, 'username' : 'warehousemanager', 'salutation' : 'Mr.', 
								  'first_name' : 'Warehouse', 'last_name' : 'Manager', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 8, 
								  'role' : 2, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 10, 'username' : 'accountingstaff', 'salutation' : 'Mr.', 
								  'first_name' : 'Accounting', 'last_name' : 'Staff', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 1, 
								  'role' : 1, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 11, 'username' : 'financestaff', 'salutation' : 'Mr.', 
								  'first_name' : 'Finance', 'last_name' : 'Staff', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 2, 
								  'role' : 1, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 12, 'username' : 'hrstaff', 'salutation' : 'Mr.', 
								  'first_name' : 'HR', 'last_name' : 'Staff', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 3, 
								  'role' : 1, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 13, 'username' : 'itstaff', 'salutation' : 'Mr.', 
								  'first_name' : 'IT', 'last_name' : 'Staff', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 4, 
								  'role' : 1, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 14, 'username' : 'purchasestaff', 'salutation' : 'Mr.', 
								  'first_name' : 'Purchase', 'last_name' : 'Staff', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 5, 
								  'role' : 1, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 15, 'username' : 'salestaff', 'salutation' : 'Mr.', 
								  'first_name' : 'Sale', 'last_name' : 'Staff', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 6, 
								  'role' : 1, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 16, 'username' : 'servicestaff', 'salutation' : 'Mr.', 
								  'first_name' : 'Service', 'last_name' : 'Staff', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 7, 
								  'role' : 1, 'notes' : 'great'}, 
								 {'is_auth' : 1, 'auth_user' : 17, 'username' : 'warehousestaff', 'salutation' : 'Mr.', 
								  'first_name' : 'Warehouse', 'last_name' : 'Staff', 'gender' : 'Male', 
								  'address' : 'address0', 'zip_code' : '11111',  
								  'city' : 'city0', 'country' : 'country0', 'phone' : ['3', '4'], 
								  'email' : ['a@stifix.com','b@stifix.com'], 'ym' : ["a","b"], 
								  "bank" : 1, 'account_no' : '111', "branch" : 1, "department" : 8, 
								  'role' : 1, 'notes' : 'great'}, ] )

		""" create index """
		""" index 0 """
		# create index : bank
		db.executesql('CREATE INDEX idx_bank ON bank (id, name);')

		# create index : company
		db.executesql('CREATE INDEX idx_company ON company (id, name);')

		# create index : department
		db.executesql('CREATE INDEX idx_department ON department (id, name);')

		# create index : role
		db.executesql('CREATE INDEX idx_role ON role (id, name);')

		""" index 1 """
		# create index : branch
		db.executesql('CREATE INDEX idx_branch ON branch (id, city, country, company);')

		# create index : customer
		db.executesql('CREATE INDEX idx_customer ON customer (id, first_name, last_name);')

		# create index : supplier
		db.executesql('CREATE INDEX idx_supplier ON supplier (id, first_name, last_name);')

		""" index 2 """
		# create index : employee
		db.executesql('CREATE INDEX idx_employee ON employee (id, first_name, last_name);')

		""" index 3 """
		# create index : acknowledgement_of_work_result
		db.executesql('CREATE INDEX idx_acknowledgement_of_work_result ON acknowledgement_of_work_result (id, acknowledgement_of_work_result_no, acknowledgement_of_work_result_date);')

		# create index : official_travel
		db.executesql('CREATE INDEX idx_official_travel ON official_travel (id, official_travel_no, official_travel_date);')

	session.flash = T('Installation Done')
	redirect(URL('default', 'index') )