from src.RowGateway.RowGateway_polymorphism.RowGateway  import RowGateway 
from src.validation.validations_methods_products import *
from src.validation.validations_methods_supplier import *
from src.validation.validations_methods_purchase import *

class PurchaseRowGateway(RowGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)

    def create(self):
        name_of_the_product = check_existance_of_product_name(self.database_connector)
        product_id = get_product_id_by_name(self.database_connector,name_of_the_product)
        quantity = validate_quantity()   
        query = "SELECT quantity FROM Products WHERE name = %s "
        quantity_in_stock= self.database_connector.execute_query(query, (name_of_the_product,)) 
        print(f"zadane mnozstvi : {quantity}")

        while True:
                #validate id
                is_id = validate_number("dodavatele")
                #check existance of id
                id_supplier = check_existance_of_supplier_id(self.database_connector,is_id)
            
                if id_supplier == True:
                        query = "SELECT price FROM Products WHERE name = %s "
                        price_of_the_product = self.database_connector.execute_query(query, (name_of_the_product,)) 
                        price_for_supplier = price_of_the_product[0][0] * quantity
                        query = "UPDATE Products SET quantity = %s  WHERE product_id = %s "
                        self.database_connector.execute_query_with_commit(query, (quantity_in_stock[0][0] + quantity,product_id))

                        query = "INSERT INTO  Purchases(product_id,supplier_id,quantity,price) VALUES(%s,%s,%s,%s)"
                        self.database_connector.execute_query_with_commit(query, (product_id,is_id,quantity,price_for_supplier)) 
                        print("\nUspesne jste vytvorili dodavku!\n")
                        break
                else:
                    print("Toto id neexistuje. Zkuste to znovu.")
   
   
   
    def edit(self):
        while True:
            purchase_id = input("Zadejte id dodavky kterou chcete upravit :")
            if purchase_id.isdigit():
                purchase_id_exist = check_existance_of_purchase_id(self.database_connector,purchase_id)
                if purchase_id_exist:
                    break
                else:
                    print("Toto id neexistuje. Zkuste to znovu")
            else:
                print("Id musi byt cislo. Zkuste to znovu")

        name = str(input("Zadejte  kategorii kterou chcete upravit :\n 1) Produkt\n 2) Dodavatel\n 3) Mnozstvi \n 4) Cena \n 5) Datum"))
        match name.capitalize():
            case "1":
                name_of_the_product = check_existance_of_product_name(self.database_connector)
                id_of_the_product = get_product_id_by_name(self.database_connector,name_of_the_product)
                query = "UPDATE Purchases SET product_id = %s WHERE purchase_id  = %s "
                self.database_connector.execute_query_with_commit(query, (id_of_the_product,purchase_id)) 
                print("\nUspesne jste upravili produkt objednavky!\n")
            case "2":
                name_of_the_supplier = check_existance_of_supplier_name(self.database_connector)
                id_of_the_supplier = get_supplier_id_by_name(self.database_connector,name_of_the_supplier)
                query = "UPDATE Purchases SET supplier_id = %s WHERE purchase_id  = %s "
                self.database_connector.execute_query_with_commit(query, (id_of_the_supplier,purchase_id)) 
                print("\nUspesne jste upravili zakaznika objednavky!\n")
            case "3":
                while True:
                    amount = input("Zadejte nove mnozstvi v objednavce : ")
                    if amount.isdigit():
                        #check enough at stock
                        query = "SELECT Products.quantity,Purchases.quantity,Products.product_id FROM Purchases inner join Products on  Products.product_id = Purchases.product_id WHERE Purchases.purchase_id = %s "
                        amount_at_stock = self.database_connector.execute_query(query, (purchase_id,))
                        print(f"pocet produktu na sklade : {amount_at_stock[0][0]}")
                        print(f"puvodni mnozstvi v dodavce : {amount_at_stock[0][1]}")
                        

                        query = "UPDATE Purchases SET quantity = %s WHERE purchase_id  = %s "
                        self.database_connector.execute_query_with_commit(query, (amount,purchase_id))
                        print(f"Novy pocet produktu na sklade : {amount_at_stock[0][0] + int(amount) -  amount_at_stock[0][1]   }")
                        query = "UPDATE Products SET quantity = %s WHERE product_id  = %s "
                        self.database_connector.execute_query_with_commit(query, (amount_at_stock[0][0] + int(amount) -  amount_at_stock[0][1] ,amount_at_stock[0][2])) 
                        print("\nUspesne jste upravili mnozstvi produktu v  objednavky!\n")
                        break
                       
                    else:
                        print("Zadejte kladne cislo. Zkuste to znova. ")

            case "4":
                while True:
                    new_price_of_sale = input("Zadejte novou cenu dodavky : ")
                    if new_price_of_sale.isdigit():
                        query = "UPDATE Purchases SET price = %s WHERE purchase_id  = %s "
                        self.database_connector.execute_query_with_commit(query, (new_price_of_sale,purchase_id))
                        print("\nUspesne jste upravili cenu dodavky\n")
                        break
                    else:
                        print("Cena musi byt cislo. Zkuste to znovu")
            case "5":
                new_date = validate_date()
                query = "UPDATE Purchases SET date = %s WHERE purchase_id  = %s "
                self.database_connector.execute_query_with_commit(query, (new_date,purchase_id))
                print("\nUspesne jste upravili datum objednavkly\n")
            case _:
                print("\nTato volba není dostupná \n")
    def delete(self):
        while True:
            id_purchase = input("Zadejte id dodavky kterou chcete smazat")
            id_purchase_exist = check_existance_of_purchase_id(self.database_connector,id_purchase)
            if id_purchase_exist:
                query = "DELETE FROM Purchases WHERE purchase_id  = %s "
                self.database_connector.execute_query_with_commit(query, (id_purchase,))
                print("\nUspesne jste smazali dodavku ze systemu\n")
                break
            else:
                print("Toto id dodavky neexistuje!")

