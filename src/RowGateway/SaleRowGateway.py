from src.RowGateway.RowGateway_polymorphism.RowGateway  import RowGateway 
from src.validation.validations_methods_sale import *
from src.validation.validations_methods_products import *
from src.validation.validations_methods_supplier import *

class SaleRowGateway(RowGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
        self.name = None

    def create(self):
        name_of_the_product = check_existance_of_product_name(self.database_connector)
        product_id = get_product_id_by_name(self.database_connector,name_of_the_product)
        enough_product_in_stock = False
        quantity = validate_quantity()   
        query = "SELECT quantity FROM Products WHERE name = %s "
        quantity_in_stock= self.database_connector.execute_query(query, (name_of_the_product,)) 
        print(f"zadane mnozstvi : {quantity}\n na sklade : {quantity_in_stock[0][0]}")
        if quantity <= quantity_in_stock[0][0]:
            print("\nMate dostatek mnozstvi produktu na sklade\n")
            enough_product_in_stock = True
        else:
            print(f"Nemate dostatek tohoto zbozi na sklade\n Aktualni pocet {name_of_the_product} na sklade : {quantity_in_stock[0][0]}")
        if enough_product_in_stock:
            while True:
                #validate id
                is_id = validate_number("zakaznika")
                #check existance of id
                id_customer = check_existance_of_id_customer(is_id,"Customers",self.database_connector)
            
                if id_customer == True:
                        query = "SELECT price FROM Products WHERE name = %s "
                        price_of_the_product = self.database_connector.execute_query(query, (name_of_the_product,)) 
                        price_for_sale = price_of_the_product[0][0] * quantity
                        query = "UPDATE Products SET quantity = %s  WHERE product_id = %s "
                        self.database_connector.execute_query_with_commit(query, (quantity_in_stock[0][0] - quantity,product_id))

                        query = "INSERT INTO  Sales(product_id,customer_id,quantity,price) VALUES(%s,%s,%s,%s)"
                        self.database_connector.execute_query_with_commit(query, (product_id,is_id,quantity,price_for_sale)) 
                        print("\nUspesne jste vytvorili objednavku!\n")
                        break
                else:
                    print("Toto id neexistuje. Zkuste to znovu.")
   
   
   
    def edit(self):
        name = str(input("Zadejte jmeno kategoriie kteoru chcete upravit : "))
        exists = check_existance_of_category_name(name,self.database_connector)
        if exists:
            new_name = validate_category_name()
            query = "UPDATE Categories SET name = %s WHERE name = %s "
            self.database_connector.execute_query_with_commit(query, (new_name,name)) 
            print("\nUspesne jste upravili jmeno kategorie!\n")
        else:
            print("Toto jmeno kategorie neexistuje")
    def delete(self):
        name = str(input("Zadejte jmeno kategoriie kteoru chcete smazat : "))
        exists = check_existance_of_category_name(name,self.database_connector)
        category_id = get_category_id(name,self.database_connector)
        print(category_id)
        if exists:
            #Update existing products with this category
            query = "UPDATE Products SET category_id = %s WHERE category_id = %s "
            self.database_connector.execute_query_with_commit(query, (None,category_id)) 
            #Delete category
            query = "DELETE FROM Categories where category_id = %s"
            self.database_connector.execute_query_with_commit(query, (category_id,)) 

            print("\nUspesne jste smazali kategorii!\n")
        else:
            print("Toto jmeno kategorie neexistuje")



