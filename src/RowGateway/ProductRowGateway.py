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
        print("edit")
    def delete(self):
        print("delete")


