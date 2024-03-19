import json 
from src.RowGateway.PurchaseRowGateway import PurchaseRowGateway
from src.TableGateway.PurchaseTableGateway import PurchaseTableGateway
from src.config.database_connector import DatabaseConnector

connector =  DatabaseConnector('config/config.ini')
purchase_row = PurchaseRowGateway(connector)
purchase_table = PurchaseTableGateway(connector)

class purchase_manager:
    def __init__(self):
        pass
    def execute(self,value,role_id):
        match value:
            case "1":
                purchase_row.create()
            case "2":
                purchase_row.edit()
            case "3":
                purchase_row.delete()
            case "4":
                purchase_table.get_all_purchases()
            case "5":
                purchase_table.get_specific_purchase()
            case _:
                print("\nTato volba není dostupná \n")
    def print_purchase_options(self,path_to_purchase_options):
        with open(path_to_purchase_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")