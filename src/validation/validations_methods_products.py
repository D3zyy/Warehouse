import re 

def validate_price():
    while True:
        price_str = input("Zadejte cenu za jeden kus: ")
        try:
            price = float(price_str)
            if price >= 0:
                return price
            else:
                print("Cena musí být nezáporné číslo. Zkuste to znovu.")
        except ValueError:
            print("Zadejte platné číslo.")

def validate_product_name():

    while True:
        username = input(f"Zadejte jmeno produktu : ")
        if username.isdigit():
            print("Jmeno nemuze byt cislo, zkuste znovu.")
        elif not (re.match(r'^[a-zA-Z .]{3,}$', username) and len(username) >= 3):
            print("Jmeno muze obsahovat pouze pismena, tečky a mezery a musi mit minimalne 3 znaky. Zkuste to znovu.")
        else:
            return username
        
def validate_quantity():
    while True:
        quantity_str = input("Zadejte množství produktu: ")
        try:
            quantity = int(quantity_str)
            if quantity >= 0:
                return quantity
            else:
                print("Množství musí být kladné celé číslo. Zkuste to znovu.")
        except ValueError:
            print("Zadejte platné celé číslo.")
def check_existance_of_product_id(connector):
    while True:
        id = input("Zadejte ID produktu, který chcete upravit: ")
        if id.isdigit() and int(id) > 0:
            query = "SELECT product_id FROM Products WHERE product_id = %s"
            result = connector.execute_query(query, (id,))
            if result:
                return id
            else:
                return False
        else:
            print("Zadejte kladné číslo. Zkuste to znovu.")
