from src.TableGateway.TableGateway_polymorphism.TableGateway  import TableGateway 


class SupplierTableGateway(TableGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
    def get_all_suppliers(self):
        print("\n")
        query = "SELECT supplier_id,name,contact_number FROM Suppliers;"
        rows = self.database_connector.execute_query(query)
        print("Zakaznici :\n")
        print("{:<5} {:<30} {:<30}".format("ID", "jmeno","Telefon"))
        print("-" * 55)
        for row in rows:
            print("{:<5} {:<30} {:<30}".format(row[0], row[1], row[2] ))
        print("\n")