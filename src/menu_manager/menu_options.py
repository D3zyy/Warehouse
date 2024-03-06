from src.config.Initialization import Settings
import json
from src.menu_manager.supplier_manager import supplier_manager

supplier_mng = supplier_manager()

#Cesta uvedena relativně kde je importován menu_options v main.py
settings1 = Settings('config/config.ini')
options = {}

class Options_manager:
    def __init__(self) -> None:
        pass
    def print_options(self,path_to_option_json):
        with open(path_to_option_json) as json_file:
            options_from_json = json.load(json_file)
            options.update(options_from_json)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")
    def welcome_message(self):
        print(f"Welcome to {settings1.warehouse_name} \n")
    def select_option(self):
        choice = str(input())
        match choice:
            case "1":
                supplier_mng.print_supplier_options('menu_manager/options_customer.json')
                choice = str(input())
                supplier_mng.execute(choice)   
            case "2":
                print("tady 2")
               
            case "3":
                print("tady 3")
                
            case _:
                print("\nTato volba není dostupná\n")
        #print(f"funguje : {options}")



#welcome_message()
##print_options('options.json')
