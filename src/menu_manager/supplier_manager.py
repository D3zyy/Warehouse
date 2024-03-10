import json 
from validation.validations_methods_supplier import *
from src.config.database_connector import DatabaseConnector
from src.RowGateway.SupplierRowGateway import SupplierRowGateway

options_supplier = {}
connector =  DatabaseConnector('config/config.ini')
supp_row = SupplierRowGateway(connector)
class supplier_manager:
    def __init__(self):
        pass
    def execute(self,value,role_id):
        match value:
            case "1":
                if role_id != 4:
                    supp_row.create()
                else:
                    print("Nemate  dostatecne pravomoce provest tento prikaz\n")
            case "2":
                if role_id != 4:
                    supp_row.update()
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