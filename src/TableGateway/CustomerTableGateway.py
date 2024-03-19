from src.TableGateway.TableGateway_polymorphism.TableGateway  import TableGateway 


class CustomerTableGateway(TableGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
    def get_all_customers(self):
        print("\n")
        query = "SELECT customer_id,name,contact_number FROM Customers;"
        rows = self.database_connector.execute_query(query)
        print("Zakaznici :\n")
        print("{:<5} {:<20} {:<20}".format("ID", "jmeno","Telefon"))
        print("-" * 50)
        for row in rows:
            print("{:<5} {:<20} {:<20}".format(row[0], row[1], row[2] ))
        print("\n")