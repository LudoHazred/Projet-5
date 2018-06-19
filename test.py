import requests
import json
import mysql.connector
from constant import *

categories_selec = CATEGORIES_SELEC
db_name = DB_NAME
db_pwd = DB_PWD
db_user = DB_USER

'''Connection to the database'''
db = mysql.connector.connect(user='{}'.format(db_user), password='{}'.format(db_pwd), host='localhost', database='{}'.format(db_name))
cursor = db.cursor()

'''For Shell'''
db = mysql.connector.connect(user='pbadmin', password='admin', host='localhost', database='purbeurre')

'''request for categories'''
r_cat = requests.get('https://fr.openfoodfacts.org/categories&json=1')
data_json = r_cat.json()
serial_data = json.dumps(data_json)
add_category = ("INSERT INTO Category" "(category)" "VALUES (%(name)s)")
cursor = db.cursor()
cursor.execute("""INSERT INTO Category(category) VALUES(%(category)s)""", data_json)
cursor.execute(add_category, serial_data)
db.commit()
cursor.close()
db.close()

'''insert values into the table Category'''
add_category = ("INSERT INTO Category"
    "(category)"
    "VALUES (%s)"
    )

payload = {
    'action': 'process',
    'tagtype_0': 'categories', #which subject is selected (categories)
    'tag_contains_0': 'contains', #contains or not
    'tag_0': '{}'.format(categories_selec), #parameters to choose
    'sort_by': 'unique_scans_n',
    'page_size': 50,
    'countries': 'France',
    'json': 1,
    'page': 1
    }

r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
data_json = r.json()
adresse = print(r.url)

data = {}
data['categories'] = []
data['categories'].append({
	'name'
	})
with open('database.json', 'w') as outfile:  
    json.dump(data, outfile)