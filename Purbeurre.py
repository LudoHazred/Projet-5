import mysql.connector
import requests
from Classes import *
from constant import *

db_host = DB_HOST
db_name = DB_NAME
db_pwd = DB_PWD
db_user = DB_USER

db_con = DBRel(db_user, db_pwd, db_host, db_name)

db_con.clear()

db_con.create()

Testu = OpenFood()

Testu.get_category(10)

Testu.get_food(5)

loop = 1

while loop:
	user_choice = int(input())

    if user_choice == 1:
        print("Bravo")

    if user_choice == 2:
        print("Pas Bravo")
    elif user_choice == 3:
    	quit()
    	sys.exit()
