from src.RowGateway.RowGateway_polymorphism.RowGateway  import RowGateway 
from src.validation.validations_methods_category import *


class CategoryRowGateway(RowGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
        self.name = None

    def create(self):
        name = validate_category_name()
        query = "INSERT INTO Categories(name)  VALUES(%s)"
        self.database_connector.execute_query_with_commit(query, (name,)) 
        print("\nUspesne jste vytvorili novou kategorii!\n")
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



