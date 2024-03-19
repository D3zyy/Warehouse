import json 
from src.RowGateway.CategoryRowGateway import CategoryRowGateway
from src.RowGateway.ProductRowGateway import ProductRowGateway
from src.config.database_connector import DatabaseConnector
from src.TableGateway.ProductsTableGateway import ProductTableGateway
from src.TableGateway.CategoriesTableGateway import CategoryTableGateway

connector =  DatabaseConnector('config/config.ini')
product_row = ProductRowGateway(connector)
category_row = CategoryRowGateway(connector)
product_table = ProductTableGateway(connector)
category_table = CategoryTableGateway(connector)

class warehouse_manager:
    def __init__(self):
        pass
    def execute(self,value,role_id):
        match value:
            case "1":
                choice = input(" 1) pridat produkt\n 2) editovat produkt \n 3) smazat produkt \n 4) zobrazit vsechny produkty na sklade \n")
                match choice:
                    case "1":
                        print(role_id)
                        if role_id != 4 and role_id !=3:
                            product_row.create()
                        else:
                            print("Pristup zamitnut")
                    case "2":
                        if role_id != 4 and role_id !=3:
                            product_row.edit()
                        else:
                            print("Pristup zamitnut")
                    case "3":
                        if role_id != 4 and role_id !=3:
                            product_row.delete()
                        else:
                            print("Pristup zamitnut")
                    case "4":
                        if role_id != 4 and role_id !=3:
                            product_table.get_all_products()
                        else:
                            print("Pristup zamitnut")
                    case _:
                         print("\nTato volba není dostupná \n")
            case "2":
                choice = input(" 1) pridat kategorii\n 2) editovat kategorii \n 3) smazat kategorii \n 4) zobrazit vsechny kategorie")
                match choice:
                    case "1":
                        if role_id != 4 and role_id !=3:
                            category_row.create()
                        else:
                            print("Pristup zamitnut")
                    case "2":
                        if role_id != 4 and role_id !=3:
                            category_row.edit()
                        else:
                            print("Pristup zamitnut")
                    case "3":
                        if role_id != 4 and role_id !=3:
                         category_row.delete()
                        else:
                            print("Pristup zamitnut")
                    case "4":
                        if role_id != 4 and role_id !=3:
                            category_table.get_all_categories()
                        else:
                            print("Pristup zamitnut")
                    case _:
                         print("\nTato volba není dostupná \n")
                


            case _:
                print("\nTato volba není dostupná \n")


    def print_warehouse_options(self,path_to_warehouse_options):
        with open(path_to_warehouse_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")