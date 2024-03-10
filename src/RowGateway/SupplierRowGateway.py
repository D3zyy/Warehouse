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
                #validate id
                is_id = validate_number("dodavatele")
                 #check existance of id
                id_supplier = check_existance_of_id_supplier(is_id,"Suppliers",self.database_connector)
     
                if id_supplier == True:
                        atribute = choice_atribute()
                        if atribute == 1:
                              new_name_of_supplier =  validate_name("dodavatele")

                              query = "UPDATE Suppliers SET name = %s WHERE supplier_id = %s"
                             
                              self.database_connector.execute_query_with_commit(query, (new_name_of_supplier,is_id))
                              self.name = new_name_of_supplier
                              print("\nUspesne jste upravili dodavatele!\n") 
                              break
                        elif atribute == 2:
                              
                                new_address_id = validate_number("adresy")
                                id_address_exist = check_existance_of_id(new_address_id,"Addresses",self.database_connector)
                                if id_address_exist == True:
                                        self.address_id = id_address_exist
                                        query = "UPDATE Suppliers SET address_id = %s WHERE supplier_id = %s"
                                        self.database_connector.execute_query_with_commit(query, (new_address_id,is_id))
                                        print("\nUspense jste upravili id adresy u dodavatele!")
                                        break
                                        
                                else:
                                        print("Toto id neexistuje. Zkuste to znovu.")
                        elif atribute == 3:
                               phone_number = validate_phone_number()
                               query = "UPDATE Suppliers SET contact_number = %s WHERE supplier_id = %s"
                               self.database_connector.execute_query_with_commit(query, (phone_number,is_id))
                               print("\nUspense jste upravili kontaktni telefon dodavatele!\n")
                               break
                else:
                    print("Toto id neexistuje. Zkuste to znovu.")
    def delete(self):
        while True:
              #validate id
                is_id = validate_number("dodavatele")
                 #check existance of id
                id_supplier = check_existance_of_id_supplier(is_id,"Suppliers",self.database_connector)
                if id_supplier == True:
                    query = "DELETE FROM Suppliers  WHERE supplier_id = %s"
                    self.database_connector.execute_query_with_commit(query, (is_id,))
                    print("\nUspense jste smazali  dodavatele!\n")
                    break 
                else:
                    print("Toto id neexistuje. Zkuste to znovu.")