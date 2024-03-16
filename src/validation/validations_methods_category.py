import re

def validate_category_name():

    while True:
        username = input(f"Zadejte jmeno kategorie : ")
        if username.isdigit():
            print("Jmeno nemuze byt cislo, zkuste znovu.")
        elif not (re.match(r'^[a-zA-Z .]{3,}$', username) and len(username) >= 3):
            print("Jmeno muze obsahovat pouze pismena, tečky a mezery a musi mit minimalne 3 znaky. Zkuste to znovu.")
        else:
            return username
def check_existance_of_category_name(name,connector):
       
       query = f"SELECT name FROM Categories WHERE name = %s "
       result = connector.execute_query(query, (name,))
       if result:
             return True
       else: 
             return False
def get_category_id(name,connector):
       query = f"SELECT category_id FROM Categories WHERE name = %s "
       result = connector.execute_query(query, (name,))
       if result:
             print(f"id kategorie : {result[0][0]}")
             return result[0][0]
       else: 
             return False