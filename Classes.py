import requests
import json
import mysql.connector
from constant import *

class OpenFood:

    def __init__(self):
        '''Initialization username, password, database name and categories'''
        self.categories_selec = CATEGORIES_SELEC
        self.db_name = DB_NAME
        self.db_pwd = DB_PWD
        self.db_user = DB_USER

        '''connection to the database'''
        self.db = mysql.connector.connect(user='{}'.format(self.db_user), password='{}'.format(self.db_pwd), host='localhost', database='{}'.format(self.db_name))

    def get_category(self):
        '''get categories from the URL API'''
        r_cat = requests.get('https://fr.openfoodfacts.org/categories&json=1')
        data_json = r_cat.json()
        data_tags = data_json.get('tags')
        data_cat = test_cat = [d.get('name', 'None') for d in test]
        i=2
        while i < 7:
            self.cursor = db.cursor()
            add_category = ("INSERT INTO Category" "(category)" "VALUES('{}')".format(test_cat[i]))
            self.cursor.execute(add_category)
            self.db.commit()
            self.cursor.close()
            i=i+1

    def get_food(self, nb_food):
        '''Parameters and request to the URL API'''
        self.payload = {
            'action': 'process',
            'tagtype_0': 'categories', #which subject is selected (categories)
            'tag_contains_0': 'contains', #contains or not
            'tag_0': '{}'.format(categories_selec), #categories to choose
            'sort_by': 'unique_scans_n',
            'page_size': 50,
            'countries': 'France',
            'json': 1,
            'page': 1
            }

        r_food = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=self.payload)
        food_json = r_food.json()
        add_food = ("INSERT INTO Food" "")
        self.cursor.execute(add_food, food_json)
        db.commit()