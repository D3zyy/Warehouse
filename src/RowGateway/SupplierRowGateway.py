from src.RowGateway.RowGateway_polymorphism.RowGateway  import RowGateway 
from validation.validations_methods_supplier import *

class SupplierRowGateway(RowGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
        self.name = None
        self.address_id = None
        self.contact_number = None
    def create(self):
        name_of_supplier =  validate_name("dodavatele")
        new_address_ = new_address()
        #Add existing address
        if new_address_ == False:
            while True:
                new_address_id = validate_number("adresy")
                id_address_exist = check_existance_of_id(new_address_id,"Addresses",self.database_connector)
                if id_address_exist == True:
                        self.address_id = id_address_exist
                        break
                else:
                    print("Toto id neexistuje. Zkuste to znovu.")
            phone_number = validate_phone_number()
            query = "INSERT INTO  Suppliers(name,address_id,contact_number) VALUES(%s,%s,%s)"
            result = self.database_connector.execute_query_with_commit(query, (name_of_supplier,new_address_id,phone_number)) 
            print("Uspesne jste vytvorili noveho dodavatele! \n")
        #Create new address
        elif new_address_ == True:
                        street_name =validate_street()
                        city_name = validate_city()
                        postal_code = validate_postal_code()
                        query = "INSERT INTO  Addresses(street,city,postal_code) VALUES(%s,%s,%s)"
                        new_address_id = self.database_connector.execute_query_with_commit(query, (street_name,city_name,postal_code))
                        print("\nUspesne jste vytvorili adresu \n")
                        query = "SELECT COUNT(address_id) FROM Addresses WHERE %s = %s"
                        addres = self.database_connector.execute_query(query, (1, 1))
                        phone_number = validate_phone_number()
                        query = "INSERT INTO  Suppliers(name,address_id,contact_number) VALUES(%s,%s,%s)"
                        print(addres[0][0])
                        result = self.database_connector.execute_query_with_commit(query, (name_of_supplier,addres[0][0],phone_number)) 
                        print("Uspesne jste vytvorili noveho dodavatele! \n")
    def update(self):
        while True:
                is_id = validate_number("dodavatele")
                print(is_id)
                id_supplier = check_existance_of_id_supplier(is_id,"Suppliers",self.database_connector)
                print(id_supplier)
                if id_supplier == True:
                        atribute = choice_atribute()
                        if atribute == 1:
                              new_name_of_supplier =  validate_name("dodavatele")
                              print(new_name_of_supplier)
                              query = "UPDATE Suppliers SET name = %s WHERE supplier_id = %s"
                              print(f"id upravujici ho ::: {is_id}")
                              result = self.database_connector.execute_query_with_commit(query, (new_name_of_supplier,is_id))
                              print("\nUspesne jste upravili dodavatele!\n") 
                              break
                        elif atribute == 2:
                              print("adress id")
                        elif atribute == 3:
                              print("telefoni cislo")
                else:
                    print("Toto id neexistuje. Zkuste to znovu.")
    def delete(self):
        query = "SELECT * FROM Roles"
        rows = self.database_connector.execute_query(query)
        self.database_connector.close_connection()
        print("Role Report:")
        print("{:<5} {:<20}".format("ID", "Name"))
        print("-" * 60)
        for row in rows:
            print("{:<5} {:<20}".format(row[0], row[1]))