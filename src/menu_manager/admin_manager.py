import json 
from src.config.database_connector import DatabaseConnector
from src.RowGateway.UserRowGateway import UserRowGateway
from vendor.printer import Printer

_printer = Printer()
connector =  DatabaseConnector('config/config.ini')
user_row = UserRowGateway(connector)


class admin_manager:
    def __init__(self):
        pass
    def execute(self,value,login_mng):
        match value:
            case "1":
                user_row.create()
            case "2":
                user_row.update(login_mng)
            case "3":
                user_row.delete()
            case "4":
                print("Zobrazit vsechny uzivatele")
            case "5":
                print("Vymazat vsechny data")
            case "6":
                print("Nacist testovaci data")
            case "7":
                print("Obnovit system")
            case _:
                print("\nTato volba není dostupná \n")
    def print_manager_options(self,path_to_manager_options):
        _printer.print_admin_section()
        with open(path_to_manager_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")