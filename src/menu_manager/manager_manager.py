import json 
from src.config.database_connector import DatabaseConnector
from printer.printer import Printer
from src.RowGateway.UserRowGateway import UserRowGateway
from src.TableGateway.UsersTableGateway import UserTableGateway


_printer = Printer()
connector =  DatabaseConnector('config/config.ini')
user_row = UserRowGateway(connector)
user_table = UserTableGateway(connector)

class manager_manager:
    def __init__(self):
        pass
    def execute(self,value,login_mng):
        match value:
            case "1":
                user_row.create(login_mng)
            case "2":
                user_row.update(login_mng)
            case "3":
                user_row.delete(login_mng)
            case "4":
                user_table.get_specific_user(login_mng)
            case _:
                print("Tato volba neni dostupna")
    def print_manager_options(self,path_to_manager_options):
        _printer.print_manager_section()
        with open(path_to_manager_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")