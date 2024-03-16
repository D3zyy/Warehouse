import json 
from src.RowGateway.CategoryRowGateway import CategoryRowGateway
from src.RowGateway.ProductRowGateway import ProductRowGateway
from src.config.database_connector import DatabaseConnector


connector =  DatabaseConnector('config/config.ini')
product_row = ProductRowGateway(connector)
category_row = CategoryRowGateway(connector)


class warehouse_manager:
    def __init__(self):
        pass
    def execute(self,value,role_id):
        match value:
            case "1":
                choice = input(" 1) pridat produkt\n 2) editovat produkt \n 3) smazat produkt \n 4) zobrazit vsechny produkty na sklade \n")
                match choice:
                    case "1":
                        print("Pridat")
                    case "2":
                        print("Editovat")
                    case "3":
                        print("smazat")
                    case "4":
                        print("Zobrazit vsechny produkty na sklade")
                    case _:
                         print("\nTato volba není dostupná \n")
            case "2":
                choice = input(" 1) pridat kategorii\n 2) editovat kategorii \n 3) smazat kategorii \n")
                match choice:
                    case "1":
                        category_row.create()
                    case "2":
                        category_row.edit()
                    case "3":
                        category_row.delete()
                    case _:
                         print("\nTato volba není dostupná \n")
                


            case _:
                print("\nTato volba není dostupná \n")


    def print_warehouse_options(self,path_to_warehouse_options):
        with open(path_to_warehouse_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")