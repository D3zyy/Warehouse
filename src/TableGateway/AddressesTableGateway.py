from src.TableGateway.TableGateway_polymorphism.TableGateway  import TableGateway 


class AddressesTableGateway(TableGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
    def get_all_addresses(self):
        print("\n")
        query = "SELECT * FROM Addresses;"
        rows = self.database_connector.execute_query(query)
        print("Adresy :\n")
        print("{:<5} {:<30} {:<15} {:<10}".format("ID", "Ulice","Mesto","PSC"))
        print("-" * 70)
        for row in rows:
            print("{:<5} {:<30} {:<15} {:<10}".format(row[0], row[1], row[2],row[3] ))
        print("\n")
    def get_number_of_address_by_city(self):
        print("\n")
        query = "SELECT city,COUNT(address_id) as 'Pocet' FROM Addresses  group by city"
        rows = self.database_connector.execute_query(query)
        print("Adresy podle města (bez diakritiky):\n")
        print("{:<30} {:<10}".format("Mesto", "Pocet adres"))
        print("-" * 50)
        for row in rows:
            print("{:<30} {:<10}".format(row[0], row[1]))
        print("\n")
    def get_number_of_address_by_psc(self):
        print("\n")
        query = "SELECT postal_code,COUNT(address_id) as 'Pocet' FROM Addresses  group by postal_code"
        rows = self.database_connector.execute_query(query)
        print("Adresy podle města (bez diakritiky):\n")
        print("{:<30} {:<10}".format("PSC", "Pocet adres"))
        print("-" * 50)
        for row in rows:
            print("{:<30} {:<10}".format(row[0], row[1]))
        print("\n")
    def get_highest_city_with_addresses(self):
        print("\n")
        query = "SELECT city, COUNT(address_id) AS Pocet FROM Addresses GROUP BY city ORDER BY Pocet DESC LIMIT 3;"
        rows = self.database_connector.execute_query(query)
        print("Mesto s nejvice adresami:\n")
        print("{:<30} {:<10}".format("Mesto", "Pocet adres"))
        print("-" * 50)
        for row in rows:
            print("{:<30} {:<10}".format(row[0], row[1]))
        print("\n")