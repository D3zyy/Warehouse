from src.config.Initialization import Settings
import json

#Cesta uvedena relativně kde je importován menu_options v main.py
settings1 = Settings('config/config.ini')
options = {}

class Options_manager:
    def __init__(self,path_to_option_json) -> None:
        self.path_to_option_json = path_to_option_json
    def print_options(self):
        with open(self.path_to_option_json) as json_file:
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
                print("tady 1")
            case "2":
                print("tady 2")
            case "3":
                print("tady 3")
            case _:
                print("\nTato volba není dostupná\n")
        #print(f"funguje : {options}")



#welcome_message()
##print_options('options.json')
