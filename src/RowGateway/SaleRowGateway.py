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
        while True:
            sale_id = input("Zadejte id objednavky kterou chcete upravit :")
            if sale_id.isdigit():
                sale_id_exist = check_existance_of_sale_id(self.database_connector,sale_id)
                if sale_id_exist:
                    break
                else:
                    print("Toto id neexistuje. Zkuste to znovu")
            else:
                print("Id musi byt cislo. Zkuste to znovu")

        name = str(input("Zadejte  kategorii kterou chcete upravit :\n 1) Produkt\n 2) Zakaznik\n 3) Mnozstvi \n 4) Cena \n 5) Datum"))
        match name.capitalize():
            case "1":
                name_of_the_product = check_existance_of_product_name(self.database_connector)
                id_of_the_product = get_product_id_by_name(self.database_connector,name_of_the_product)
                query = "UPDATE Sales SET product_id = %s WHERE sale_id  = %s "
                self.database_connector.execute_query_with_commit(query, (id_of_the_product,sale_id)) 
                print("\nUspesne jste upravili produkt objednavky!\n")
            case "2":
                name_of_the_customer = check_existance_of_customer_name(self.database_connector)
                id_of_the_customer = get_customer_id_by_name(self.database_connector,name_of_the_customer)
                query = "UPDATE Sales SET customer_id = %s WHERE sale_id  = %s "
                self.database_connector.execute_query_with_commit(query, (id_of_the_customer,sale_id)) 
                print("\nUspesne jste upravili zakaznika objednavky!\n")
            case "3":
                while True:
                    amount = input("Zadejte nove mnozstvi v objednavce : ")
                    if amount.isdigit():
                        #check enough at stock
                        query = "SELECT Products.quantity,Sales.quantity,Products.product_id FROM Sales inner join Products on  Products.product_id = Sales.product_id WHERE Sales.sale_id = %s "
                        amount_at_stock = self.database_connector.execute_query(query, (sale_id,))
                        #print(f"pocet produktu na sklade : {amount_at_stock[0][0]}")
                        #print(f"puvodni mnozstvi v objednavce : {amount_at_stock[0][1]}")
                        if amount_at_stock[0][0] + amount_at_stock[0][1] >= int(amount):

                            query = "UPDATE Sales SET quantity = %s WHERE sale_id  = %s "
                            self.database_connector.execute_query_with_commit(query, (amount,sale_id))
                            print(f"Novy pocet produktu na sklade : {amount_at_stock[0][0] + amount_at_stock[0][1] - int(amount)}")
                            query = "UPDATE Products SET quantity = %s WHERE product_id  = %s "
                            self.database_connector.execute_query_with_commit(query, (amount_at_stock[0][0] + amount_at_stock[0][1] - int(amount),amount_at_stock[0][2])) 
                            print("\nUspesne jste upravili mnozstvi produktu v  objednavky!\n")
                            break
                        else:
                            print("\nNemate dostatek produktu na sklade\n")
                            break
                    else:
                        print("Zadejte kladne cislo. Zkuste to znova. ")

            case "4":
                while True:
                    new_price_of_sale = input("Zadejte novou cenu objednavky : ")
                    if new_price_of_sale.isdigit():
                        query = "UPDATE Sales SET price = %s WHERE sale_id  = %s "
                        self.database_connector.execute_query_with_commit(query, (new_price_of_sale,sale_id))
                        print("\nUspesne jste upravili cenu objednavkly\n")
                        break
                    else:
                        print("Cena musi byt cislo. Zkuste to znovu")
            case "5":
                new_date = validate_date()
                query = "UPDATE Sales SET date = %s WHERE sale_id  = %s "
                self.database_connector.execute_query_with_commit(query, (new_date,sale_id))
                print("\nUspesne jste upravili datum objednavkly\n")
            case _:
                print("\nTato volba není dostupná \n")
    def delete(self):
        while True:
            id_sale = input("Zadejte id objednavky kterou chcete smazat")
            id_sale_exist = check_existance_of_sale_id(self.database_connector,id_sale)
            if id_sale_exist:
                query = "DELETE FROM Sales WHERE sale_id  = %s "
                self.database_connector.execute_query_with_commit(query, (id_sale,))
                print("\nUspesne jste smazali objednavku ze systemu\n")
                break
            else:
                print("Toto id objednavky neexistuje!")

