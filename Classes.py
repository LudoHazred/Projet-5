import requests
import unidecode
import mysql.connector
from constant import *

class OpenFood:

    def __init__(self):
        '''Initialization username, password, database name and categories'''
        self.db_name = DB_NAME
        self.db_pwd = DB_PWD
        self.db_user = DB_USER

        '''connection to the database'''
        self.db = mysql.connector.connect(user='{}'.format(self.db_user), password='{}'.format(self.db_pwd), host='localhost', database='{}'.format(self.db_name))

class OpenFood:

    def __init__(self):
        self.db = mysql.connector.connect(user='pbadmin', password='admin', host='localhost', database='purbeurre')


    def get_category(self, nb_i):
        '''get categories from the URL API'''
        r_cat = requests.get('https://fr.openfoodfacts.org/categories&json=1')
        data_json = r_cat.json()
        data_tags = data_json.get('tags')
        data_cat = [d.get('name', 'None') for d in data_tags]
        i= nb_i
        while i < 7:
            self.cursor = self.db.cursor()
            add_category = ("INSERT INTO Category" "(category)" "VALUES('{}')".format(data_cat[i]))
            self.cursor.execute(add_category)
            self.db.commit()
            self.cursor.close()
            i=i+1

    def get_food(self, nb_fd):
        '''Parameters and request to the URL API'''
        for i in range(1,6):
            nb_ini_cat = i
            nb_food = nb_fd
            cursor = self.db.cursor(buffered=True)
            cat_nb_1 = str(nb_ini_cat)
            selec_cat = ("SELECT category FROM Category WHERE idCategory = "+cat_nb_1)
            cursor.execute(selec_cat)
            cat_saved = str(cursor.fetchone()[0]) #indexation
            payload = {
            'action': 'process',
            'tagtype_0': 'categories', #which subject is selected (categories)
            'tag_contains_0': 'contains', #contains or not
            'tag_0': '{}'.format(cat_saved), #parameters to choose
            'sort_by': 'unique_scans_n',
            'page_size': '{}'.format(nb_food),
            'countries': 'France',
            'json': 1,
            'page': 1
            }
            r_food = requests.get('https://fr.openfoodfacts.org/cgi/search.pl', params=payload)
            food_json = r_food.json()
            test2 = food_json.get('products')

            food_id = ("SELECT idCategory FROM Category WHERE idCategory = "+cat_nb_1)
            cursor.execute(food_id)
            food_id_saved = cursor.fetchone()[0]
    
            for x in range(nb_food) :

                prod_name_saved = [d.get('product_name_fr') for d in test2]
                prod_name = str(prod_name_saved[x])
                ingrdts_saved = [d.get('ingredients_text_fr') for d in test2]
                ingrdts = str(ingrdts_saved[x])
                ingredts = unidecode.unidecode(ingrdts)
                ingredtss = ingredts.replace("'", "")
                nutri_grd_saved = [d.get('nutrition_grade_fr') for d in test2]
                nutri_grd = str(nutri_grd_saved[x])
                bar_code_saved = [d.get('id') for d in test2]
                bar_code = bar_code_saved[x]
                add_food =(
                    "INSERT INTO Food"
                    "(idCategory, category, food, ingredient, nutriscore, bar_code)"
                    "VALUES ('{}', '{}', '{}', '{}', '{}', {})".format(food_id_saved, cat_saved, prod_name, ingredtss, nutri_grd, bar_code))
                cursor.execute(add_food)
                self.db.commit()
            cursor.close()