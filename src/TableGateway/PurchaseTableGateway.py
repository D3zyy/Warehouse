from src.TableGateway.TableGateway_polymorphism.TableGateway  import TableGateway 
from src.validation.validations_methods_sale import *

class PurchaseTableGateway(TableGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
    def get_all_purchases(self):
        print("\n")
        query = "SELECT Purchases.purchase_id,Products.name,Suppliers.name,Purchases.quantity,Purchases.price FROM Purchases inner join Products on Purchases.product_id = Products.product_id inner join Suppliers on Purchases.supplier_id = Suppliers.supplier_id"
        rows = self.database_connector.execute_query(query)
        print("Dodavky :")
        print("{:<5} {:<40} {:<30} {:<10} {:<10} ".format("ID", "Produkt", "Dodavatel","Mnozstvi","Cena"))
        print("-" * 100)
        for row in rows:
            print("{:<5} {:<40} {:<30} {:<10} {:<10} ".format(row[0], row[1] ,row[2], row[3] ,row[4] ))
        print("\n")
    def get_specific_purchase(self):
        print("\n")
        while True:
            id_ = input("Zadejte id dodavky : ")
            if id_.isdigit():
                exist = check_existance_of_sale_id(self.database_connector,id_)
                if exist:
                    break
                else:
                    print("Toto id neexistuje. Zkuste to znovu")
            else:
                print("Zadejte nezaporne cislo. Zkuste to znovu")
        query = "SELECT Purchases.purchase_id,Products.name,Suppliers.name,Purchases.quantity,Purchases.price FROM Purchases inner join Products on Purchases.product_id = Products.product_id inner join Suppliers on Purchases.supplier_id = Suppliers.supplier_id where purchase_id = %s"
        rows = self.database_connector.execute_query(query,(id_,))
        print("Dodavka :")
        print("{:<5} {:<40} {:<20} {:<10} {:<10} ".format("ID", "Produkt", "Dodavatel","Mnozstvi","Cena"))
        print("-" * 100)
        for row in rows:
            print("{:<5} {:<40} {:<20} {:<10} {:<10} ".format(row[0], row[1] ,row[2], row[3] ,row[4] ))
        print("\n")