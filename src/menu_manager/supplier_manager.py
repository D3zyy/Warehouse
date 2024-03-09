import json 
from validation.validations_methods_supplier import *
from src.config.database_connector import DatabaseConnector
options_supplier = {}
connector =  DatabaseConnector('config/config.ini')
class supplier_manager:
    def __init__(self):
        pass
    def execute(self,value,role_id):
        match value:
            case "1":
                if role_id != 4:
                    name_of_supplier =  validate_name("dodavatele")
                    new_address_ = new_address()
                    if new_address_ == False:
                        while True:
                            new_address_id = validate_number("adresy")
                            id_address_exist = check_existance_of_id(new_address_id,"Addresses",connector)
                            if id_address_exist == True:
                                break
                            else:
                                print("Toto id neexistuje. Zkuste to znovu.")
                        phone_number = validate_phone_number()
                        query = "INSERT INTO  Suppliers(name,address_id,contact_number) VALUES(%s,%s,%s)"
                        result = connector.execute_query_with_commit(query, (name_of_supplier,new_address_id,phone_number)) 
                        print("Uspesne jste vytvorili noveho dodavatele! \n")
                    elif new_address_ == True:
                        print("novou")
                        
                    #print("VYTVORENI")
                else:
                    print("Nemate  dostatecne pravomoce provest tento prikaz\n")
            case "2":
                if role_id != 4:
                    print("EDITACE")
                else:
                    print("Nemate  dostatecne pravomoce provest tento prikaz\n")
            case "3":
                if role_id != 4:
                    print("ODSTRANENI")
                else:
                    print("Nemate  dostatecne pravomoce provest tento prikaz\n")
            case _:
                print("\nTato volba není dostupná \n")
    def print_supplier_options(self,path_to_supplier_options):
        with open(path_to_supplier_options) as json_file:
            options_from_json = json.load(json_file)
            options_supplier.update(options_from_json)
            for key, value in options_from_json.items():
                print(f" {key}) {value}")