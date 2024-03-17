from src.TableGateway.TableGateway_polymorphism.TableGateway  import TableGateway 



class ProductTableGateway(TableGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
    def get_all_products(self):
        print("\n")
        query = "SELECT Products.product_id, Products.name, Products.quantity, Products.price, Categories.name FROM Products INNER JOIN Categories ON Categories.category_id = Products.category_id;"
        rows = self.database_connector.execute_query(query)
        print("Produkty na sklade:")
        print("{:<5} {:<30} {:<5} {:<10} {:<25}".format("ID", "Produkt","Pocet","Cena za kus","Kategorie produktu"))
        print("-" * 70)
        for row in rows:
            print("{:<5} {:<30} {:<5} {:<10} {:<25}".format(row[0], row[1] ,row[2], row[3], row[4]))
        print("\n")