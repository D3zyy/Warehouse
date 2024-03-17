from src.TableGateway.TableGateway_polymorphism.TableGateway  import TableGateway 



class CategoryTableGateway(TableGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
    def get_all_categories(self):
        print("\n")
        query = "SELECT category_id,name FROM Categories;"
        rows = self.database_connector.execute_query(query)
        print("Kategorie produktu :\n")
        print("{:<5} {:<30}".format("ID", "jmeno kategorie"))
        print("-" * 20)
        for row in rows:
            print("{:<5} {:<30}".format(row[0], row[1] ))
        print("\n")