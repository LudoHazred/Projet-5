import requests
import json
import records
from constant import *

def __init__(self, categories_selec):
    '''Initialization username, password, database name and categories'''
    self.categories_selec = CATEGORIES_SELEC
    self.db_name = DB_NAME
    self.db_pwd = DB_PWD
    self.db_user = DB_USER

def connect_db(self):
    '''Connect to database'''
    self.db = records.Database('mysql://{}:{}@localhost/{}'.format(self.db_user, self.db_pwd, self.db_name))
    self.db.query('USE {};'.format(self.db_name))

def get_data(self):
    self.payload = {
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
    r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=self.payload)
    self.data = r.json()

def research(self, product):
	self.db.query('')

db = records.Database('mysql://pbadmin:admin@localhost/purbeurre'.format(self.db_user, self.db_pwd, self.db_name))
