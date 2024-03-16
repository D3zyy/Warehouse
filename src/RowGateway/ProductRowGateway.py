from src.RowGateway.RowGateway_polymorphism.RowGateway  import RowGateway 
from src.validation.validations_methods_products import *
from src.validation.validations_methods_category import *


class ProductRowGateway(RowGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
        self.name = None
        self.price = None
        self.quantity = None
        self.category_id = None


    def create(self):
        name_of_the_product = validate_product_name()
        price = validate_price()
        quantity = validate_quantity()
        while True:
            category_name = input("Zadejte jmeno kategorie produktu : ")
            exists = check_existance_of_category_name(category_name,self.database_connector)
            if exists:
                category_id = get_category_id(category_name,self.database_connector)
                self.name = name_of_the_product
                self.price = price
                self.quantity = quantity
                self.category_id = category_id

                query = "INSERT INTO Products(name,price,quantity,category_id)  VALUES(%s,%s,%s,%s)"
                self.database_connector.execute_query_with_commit(query, (self.name,self.price,self.quantity,self.category_id)) 
                print("\nUspesne jste vytvorili novy produkt !\n")
                break
            else:
                print("Tato kategorie neexistuje. Zkuste to znovu")
    def edit(self):
        while True:
            id = check_existance_of_product_id(self.database_connector)
            if id:
                


                choice = input("Vyberte co chcete upravit : \n 1) jmeno produktu \n 2) cenu produktu \n 3) mnozstvi produktu \n 4) kategorii \n")
                match choice:
                    case "1":
                        new_name_of_the_product = validate_product_name()
                        query = "UPDATE Products SET name = %s where product_id = %s "
                        self.name = new_name_of_the_product
                        self.database_connector.execute_query_with_commit(query, (self.name,id)) 
                        print("\nUspesne jste upravili jmeno  produktu !\n")
                        break
                    case "2":
                        new_price = validate_price()
                        query = "UPDATE Products SET price = %s where product_id = %s "
                        self.price = new_price
                        self.database_connector.execute_query_with_commit(query, (self.price,id)) 
                        print("\nUspesne jste upravili cenu produktu !\n")
                        break
                    case "3":
                        new_quantity = validate_quantity()
                        query = "UPDATE Products SET quantity = %s where product_id = %s "
                        self.quantity = new_quantity
                        self.database_connector.execute_query_with_commit(query, (self.quantity,id)) 
                        print("\nUspesne jste upravili mnozstvi produktu na sklade !\n")
                        break
                    case "4":
                        while True:
                            category_name = input("Zadejte nove jmeno kategorie produktu : ")
                            exists = check_existance_of_category_name(category_name,self.database_connector)
                            if exists:
                                category_id = get_category_id(category_name,self.database_connector)
                                self.category_id = category_id
                                query = "UPDATE Products SET category_id = %s where product_id = %s "
                                print(f"produkt id = {id} \n kategorie id = {self.category_id}")
                                self.database_connector.execute_query_with_commit(query, (self.category_id,id)) 
                                print("\nUspesne jste upravili kategorii produktu !\n")
                                break
                            else:
                                print("Tato kategorie neexistuje. Zkuste to znovu")
                        break
            else:
                    print("Toto id neexistuje. Zkuste to znovu")
    def delete(self):
         id = check_existance_of_product_id(self.database_connector)
         if id:
            query = "DELETE FROM Products where product_id = %s "
            self.database_connector.execute_query_with_commit(query, (id,)) 
            print("\nUspesne jste smazali  produkt !\n")
         else:
             print("Toto id neexistuje. Zkuste to znovu")


