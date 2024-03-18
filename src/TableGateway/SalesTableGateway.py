from src.TableGateway.TableGateway_polymorphism.TableGateway  import TableGateway 


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