import json 
from src.RowGateway.SaleRowGateway import SaleRowGateway
from src.TableGateway.SalesTableGateway import SaleTableGateway
from src.config.database_connector import DatabaseConnector

connector =  DatabaseConnector('config/config.ini')
sale_row = SaleRowGateway(connector)
sale_table = SaleTableGateway(connector)

class sale_manager:
    def __init__(self):
        pass
    def execute(self,value,role_id):
        match value:
            case "1":
                if role_id == 1 or role_id == 2 or role_id == 3:
                    sale_row.create()
                else:
                    print("Pristup zamitnut")
            case "2":
                if role_id == 1 or role_id == 2 or role_id == 3:
                    sale_row.edit()
                else:
                    print("Pristup zamitnut")
            case "3":
                if role_id == 1 or role_id == 2 or role_id == 3:
                    sale_row.delete()
                else:
                    print("Pristup zamitnut")
            case "4":
                if role_id == 1 or role_id == 2 or role_id == 3:
                    sale_table.get_all_sales()
                else:
                    print("Pristup zamitnut")
            case "5":
                if role_id == 1 or role_id == 2 or role_id == 3:
                    sale_table.get_specific_sale()
                else:
                    print("Pristup zamitnut")
            case _:
                print("\nTato volba není dostupná \n")
    def print_sale_options(self,path_to_sale_options):
        with open(path_to_sale_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")