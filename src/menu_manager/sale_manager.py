import json 
from src.RowGateway.SaleRowGateway import SaleRowGateway
from src.config.database_connector import DatabaseConnector

connector =  DatabaseConnector('config/config.ini')
sale_row = SaleRowGateway(connector)

class sale_manager:
    def __init__(self):
        pass
    def execute(self,value,role_id):
        match value:
            case "1":
                sale_row.create()
            case "2":
                print("EDITACE")
            case "3":
                print("ODSTRANENI")
            case "4":
                print("Zobrazit vsechny objednavky")
            case "5":
                print("Zobrazit specifickou objednavku")
            case _:
                print("\nTato volba není dostupná \n")
    def print_sale_options(self,path_to_sale_options):
        with open(path_to_sale_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")