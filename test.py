import requests
import json
import mysql.connector
import unidecode
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
nb_cat = i - 2
nb_food = 50
nb_ini_cat = 1

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
adresse = print(r_food.url)

test2 = food_json.get('products')

test_food_1 = [d.get('product_name_fr') for d in test2]
test_food_2 = [d.get('ingredients_text_fr') for d in test2]
test_food_3 = [d.get('nutrition_grade_fr') for d in test2]


pouette = 0
food_id = ("SELECT idCategory FROM Category WHERE idCategory = "+cat_nb_1)
cursor.execute(food_id)
food_id_saved = str(cursor.fetchone()[0])
cat_name = ("SELECT category FROM Category WHERE idCategory = "+cat_nb_1)
cursor.execute(cat_name)
category = str(cursor.fetchone()[0])

while pouette < 10:
    cursor = db.cursor()
    add_food =(
    	"INSERT INTO Food"
    	"(idCategory, category, food, ingredient, nutriscore)"
    	"VALUES('{}, {}, {}, {}, {},')".format(food_id_saved, cat_saved, test_cat[pouette], test_cat))

'''Proche de l'ajoute base food'''
for i in range(1,6):
    nb_ini_cat = i
    nb_food = 10
    cursor = db.cursor(buffered=True)
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
        nutri_grd_saved = [d.get('nutrition_grade_fr') for d in test2]
        nutri_grd = str(nutri_grd_saved[x])
        bar_code_saved = [d.get('id') for d in test2]
        bar_code = bar_code_saved[x]
        add_food =(
            "INSERT INTO Food"
            "(idCategory, category, food, ingredient, nutriscore, bar_code)"
            "VALUES ('{}', '{}', '{}', '{}', '{}', {})".format(food_id_saved, cat_saved, prod_name, ingredts, nutri_grd, bar_code))
        cursor.execute(add_food)
        db.commit()
    cursor.close()

'''Test shell'''
db = mysql.connector.connect(user='pbadmin', password='admin', host='localhost', database='purbeurre')

nb_ini_cat = 1
nb_food = 50
cursor = db.cursor(buffered=True)
cat_nb_1 = str(nb_ini_cat)
selec_cat = ("SELECT category FROM Category WHERE idCategory = "+cat_nb_1)
cursor.execute(selec_cat)
cat_saved = str(cursor.fetchone()[0])
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

prod_name_saved = [d.get('product_name_fr') for d in test2]
prod_name = str(prod_name_saved[1])
ingrdts_saved = [d.get('ingredients_text_fr') for d in test2]
ingrdts = str(ingrdts_saved[1])
ingredientss = unidecode.unidecode(ingrdts)
nutri_grd_saved = [d.get('nutrition_grade_fr') for d in test2]
nutri_grd = str(nutri_grd_saved[1])
bar_code_saved = [d.get('id') for d in test2]
bar_code = bar_code_saved[1]
add_food =(
"INSERT INTO Food"
"(idCategory, category, food, ingredient, nutriscore, bar_code)"
"VALUES ('{}', '{}', '{}', '{}', '{}', {})".format(food_id_saved, cat_saved, prod_name, ingredientss, nutri_grd, bar_code))
cursor.execute(add_food)
db.commit()

'''TEST Class pas de format'''
class OpenFood:

    def __init__(self):
        self.db = mysql.connector.connect(user='pbadmin', password='admin', host='localhost', database='purbeurre')


    def get_category(self):
        '''get categories from the URL API'''
        r_cat = requests.get('https://fr.openfoodfacts.org/categories&json=1')
        data_json = r_cat.json()
        data_tags = data_json.get('tags')
        data_cat = [d.get('name', 'None') for d in data_tags]
        i = 2
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

                prod_name_saved = [d.get('product_name_fr') for d in test2] #get product name in french
                prod_name = str(prod_name_saved[x])
                ingrdts_saved = [d.get('ingredients_text_fr') for d in test2] #get ingredients list in french
                ingrdts = str(ingrdts_saved[x])
                '''ingredts = unidecode.unidecode(ingrdts)'''
                '''ingredts2 = ingredts.replace("'", "")'''
                '''ingredts3 = ingredts.replace("*", "")'''
                nutri_grd_saved = [d.get('nutrition_grade_fr') for d in test2] #get nutrigrade
                nutri_grd = str(nutri_grd_saved[x])
                bar_code_saved = [d.get('id') for d in test2] #get barcode
                bar_code = bar_code_saved[x]
                add_food =(
                    "INSERT INTO Food"
                    "(idCategory, category, food, ingredient, nutriscore, bar_code)"
                    "VALUES (%s, %s, %s, %s, %s, %s)")
                data = (food_id_saved, cat_saved, prod_name, ingrdts, nutri_grd, bar_code)
                cursor.execute(add_food, data)
                self.db.commit()
            cursor.close()