# -*- coding: utf-8 -*-

for table in db.tables:
	if '_archive' not in table and table != 'auth_event':
		db[table]._after_insert.append(partial(administration_event.after_insert_event, table = table) )
		db[table]._after_update.append(partial(administration_event.after_update_event, table = table) )
		db[table]._before_delete.insert(0, partial(administration_event.before_delete_event, table=table) )
