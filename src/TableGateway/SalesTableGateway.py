from src.TableGateway.TableGateway_polymorphism.TableGateway  import TableGateway 
from src.validation.validations_methods_sale import *

class SaleTableGateway(TableGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
    def get_all_sales(self):
        print("\n")
        query = "SELECT Sales.sale_id,Products.name,Customers.name,Sales.quantity,Sales.price FROM Sales inner join Products on Sales.product_id = Products.product_id inner join Customers on Sales.customer_id = Customers.customer_id"
        rows = self.database_connector.execute_query(query)
        print("Zakazky :")
        print("{:<5} {:<40} {:<20} {:<10} {:<10} ".format("ID", "Produkt", "Zakaznik","Mnozstvi","Cena"))
        print("-" * 90)
        for row in rows:
            print("{:<5} {:<40} {:<20} {:<10} {:<10} ".format(row[0], row[1] ,row[2], row[3] ,row[4] ))
        print("\n")
    def get_specific_sale(self):
        print("\n")
        while True:
            id_ = input("Zadejte id objednavky : ")
            if id_.isdigit():
                exist = check_existance_of_sale_id(self.database_connector,id_)
                if exist:
                    break
                else:
                    print("Toto id neexistuje. Zkuste to znovu")
            else:
                print("Zadejte nezaporne cislo. Zkuste to znovu")
        query = "SELECT Sales.sale_id,Products.name,Customers.name,Sales.quantity,Sales.price FROM Sales inner join Products on Sales.product_id = Products.product_id inner join Customers on Sales.customer_id = Customers.customer_id where sale_id = %s"
        rows = self.database_connector.execute_query(query,(id_,))
        print("Zakazka :")
        print("{:<5} {:<40} {:<20} {:<10} {:<10} ".format("ID", "Produkt", "Zakaznik","Mnozstvi","Cena"))
        print("-" * 90)
        for row in rows:
            print("{:<5} {:<40} {:<20} {:<10} {:<10} ".format(row[0], row[1] ,row[2], row[3] ,row[4] ))
        print("\n")