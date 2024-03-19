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
                if role_id == 1 or role_id == 2 or role_id == 3:
                    purchase_row.create()
                else:
                    print("Pristup zamitnut")
            case "2":
                if role_id == 1 or role_id == 2 or role_id == 3:
                    purchase_row.edit()
                else:
                    print("Pristup zamitnut")
            case "3":
                if role_id == 1 or role_id == 2 or role_id == 3:
                    purchase_row.delete()
                else:
                    print("Pristup zamitnut")
            case "4":
                if role_id == 1 or role_id == 2 or role_id == 3:
                    purchase_table.get_all_purchases()
                else:
                    print("Pristup zamitnut")
            case "5":
                if role_id == 1 or role_id == 2 or role_id == 3:
                    purchase_table.get_specific_purchase()
                else:
                    print("Pristup zamitnut")
            case _:
                print("\nTato volba není dostupná \n")
    def print_purchase_options(self,path_to_purchase_options):
        with open(path_to_purchase_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")