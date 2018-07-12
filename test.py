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
with open('C:/Users/Noway/Desktop/Projet-5/data.json') as json_data:
    data_dict = json.load(json_data)
data_json = data_dict.json()
serial_data = json.dumps(data_json)
add_category = ("INSERT INTO Category" "(category)" "VALUES (%s)")
cursor = db.cursor()
cursor.execute("""INSERT INTO Category(category) VALUES(%s)""", data_json)
cursor.execute(add_category, data_dict.get(tags.name))
db.commit()
cursor.close()
db.close()

test_key = "Value : %s" % data_json.get('count')

[d.get('name', 'None') for d in list]

'''Testé et approuvé'''
r_cat = requests.get('https://fr.openfoodfacts.org/categories&json=1')
data_json = r_cat.json()
test = data_json.get('tags')
test_cat = [d.get('name', 'None') for d in test]
i=2
while i < 7:
	cursor = db.cursor()
	add_category = ("INSERT INTO Category" "(category)" "VALUES('{}')".format(test_cat[i]))
	cursor.execute(add_category)
	db.commit()
	cursor.close()
	i=i+1

'''Test de la suite'''
cursor = db.cursor(buffered=True)
nb_category = i - 2
nb_food = 50
nb_ini_cat = 1

cursor.execute(selec)
rows = cursor.fetchall()

while nb_ini_cat < nb_category:
    nb_ini_cat = str()


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