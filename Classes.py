import requests
import unidecode
import mysql.connector
from constant import *


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
        while i < 12:
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

class DBRel:

    def __init__(self, name, pwd, user, host):
		self.name = name
		self.pwd = pwd
		self.user = user
		self.host = host
		self.con = mysql.connector.connect(user=user, password=pwd, host=host, database=name)

    def clear(self):
    	self.cursor.execute("""DROP TABLE Category, Food, Substitute""")

    def create_db(self):
    	self.cursor.execute("""
    		CREATE TABLE Category (
            idCategory INT AUTO_INCREMENT NOT NULL,
            category VARCHAR(1000) NOT NULL,
            PRIMARY KEY (idCategory)
            );
            """)
    	return print("Cleared")

    	self.cursor.execute("""
            CREATE TABLE Substitute (
            id INT AUTO_INCREMENT NOT NULL,
            idCategory INT NOT NULL,
            category VARCHAR(200) NOT NULL,
            subcategory VARCHAR(200),
            ingredient VARCHAR(5000),
            nutriscore CHAR(10),
            label VARCHAR(1000),
            additive VARCHAR(1000),
            nutrient VARCHAR(1000),
            store VARCHAR(1000),
            bar_code BIGINT,
            link VARCHAR(1000),
            PRIMARY KEY (id, idCategory)
            );
            """)

    	self.cursor.execute("""
            CREATE TABLE Food (
            id INT AUTO_INCREMENT NOT NULL,
            idCategory INT NOT NULL,
            category VARCHAR(200) NOT NULL,
            food VARCHAR(400) NOT NULL,
            ingredient VARCHAR(5000),
            additive VARCHAR(1000),
            nutriscore CHAR(10),
            nutrient VARCHAR(1000),
            label VARCHAR(1000),
            store VARCHAR(1000),
            bar_code BIGINT,
            PRIMARY KEY (id, idCategory)
            );
            """)

    	self.cursor.execute("""
            ALTER TABLE Food ADD CONSTRAINT category_food_fk
            FOREIGN KEY (idCategory)
            REFERENCES Category (idCategory)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION;
            """)

    	self.cursor.execute("""
            ALTER TABLE Substitute ADD CONSTRAINT category_substitute_fk
            FOREIGN KEY (idCategory)
            REFERENCES Category (idCategory)
            ON DELETE NO ACTION
            ON UPDATE NO ACTION;
            """)
    	return print("Bases crées")