import re 

def validate_date():
    while True:
        date_input = input("Zadejte datum ve formátu YYYY-MM-DD: ")
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date_input):
            return date_input
        else:
            print("Neplatný formát! Datum musí být ve formátu YYYY-MM-DD.")


def check_existance_of_product_name(connector):
    while True:
        name = input("Zadejte jmeno produktu: ")
        if len(name) < 1:
            print("Jmeno produktu nesmi byt prazdne. Zkuste to znovu.")
        else:
            query = "SELECT name FROM Products WHERE name = %s"
            result = connector.execute_query(query, (name,))
            if result: 
                return name
            else:
                print("Produkt s timto nazvem neexistuje. Zkuste to znovu")
def get_supplier_id(id,table,connector):
       query = f"SELECT supplier_id FROM {table} WHERE supplier_id = %s "
       result = connector.execute_query(query, (id,))
       if result:
             return True
       else: 
             return False
def get_product_id_by_name(connector,name):
            query = "SELECT product_id FROM Products WHERE name = %s"
            result = connector.execute_query(query, (name,))
            if result:
                return result[0][0]
            else:
                return False
def get_supplier_id_by_name(connector,name):
            query = "SELECT supplier_id FROM Suppliers WHERE name = %s"
            result = connector.execute_query(query, (name,))
            if result:
                return result[0][0]
            else:
                return False
def check_existance_of_purchase_id(connector,id):

            query = "SELECT purchase_id FROM Purchases WHERE purchase_id = %s"
            result = connector.execute_query(query, (id,))
            if result: 
                return id
            else:
                return False
def check_existance_of_supplier_id(connector,id):

            query = "SELECT supplier_id FROM Suppliers WHERE supplier_id = %s"
            result = connector.execute_query(query, (id,))
            if result: 
                return True
            else:
                return False
def check_existance_of_supplier_name(connector):
    while True:
        name = input("Zadejte jmeno dodavatele: ")
        if len(name) < 1:
            print("Jmeno dodavatele nesmi byt prazdne. Zkuste to znovu.")
        else:
            query = "SELECT name FROM Suppliers WHERE name = %s"
            result = connector.execute_query(query, (name,))
            if result: 
                return name
            else:
                print("Dodavatel s timto nazvem neexistuje. Zkuste to znovu")
            
