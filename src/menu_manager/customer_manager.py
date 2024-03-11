import json 
from validation.validations_methods_supplier import *
from src.config.database_connector import DatabaseConnector
from src.RowGateway.CustomerRowGateway import CustomerRowGateway

connector =  DatabaseConnector('config/config.ini')
cust_row = CustomerRowGateway(connector)

class customer_manager:
    def __init__(self):
        pass
    def execute(self,value,role_id):
        match value:
            case "1":
                if role_id != 4:
                    cust_row.create()
                else:
                    print("Nemate  dostatecne pravomoce provest tento prikaz\n")
            case "2":
                if role_id != 4:
                    cust_row.update()
                else:
                    print("Nemate  dostatecne pravomoce provest tento prikaz\n")
            
            case "3":
                if role_id != 4:
                    cust_row.delete()
                else:
                    print("Nemate  dostatecne pravomoce provest tento prikaz\n")
          
            case _:
                print("\nTato volba není dostupná \n")
    def print_customer_options(self,path_to_customer_options):
        with open(path_to_customer_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")