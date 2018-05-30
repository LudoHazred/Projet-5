import records

db = records.Database('mysql://pbadmin:admin@localhost/purbeurre')
rows = db.query('USE purbeurre;')