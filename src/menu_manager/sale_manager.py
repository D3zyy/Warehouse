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
                sale_row.create()
            case "2":
                sale_row.edit()
            case "3":
                sale_row.delete()
            case "4":
                sale_table.get_all_sales()
            case "5":
                print("Zobrazit specifickou objednavku")
            case _:
                print("\nTato volba není dostupná \n")
    def print_sale_options(self,path_to_sale_options):
        with open(path_to_sale_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")