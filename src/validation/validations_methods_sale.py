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
def get_customer_id(id,table,connector):
       query = f"SELECT customer_id FROM {table} WHERE customer_id = %s "
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
           