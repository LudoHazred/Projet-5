import requests
import json
import records
from constant import *

categories_selec = CATEGORIES_SELEC
db_name = DB_NAME
db_pwd = DB_PWD
db_user = DB_USER

db = records.Database('mysql://{}:{}@localhost'.format(db_user, db_pwd))
queue = db.query('USE {};'.format(db_name))

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
data = r.json()
adresse = print(r.url)