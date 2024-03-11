import json 
from src.config.database_connector import DatabaseConnector
from src.RowGateway.UserRowGateway import UserRowGateway

connector =  DatabaseConnector('config/config.ini')
user_row = UserRowGateway(connector)

class account_manager:
    def __init__(self):
        pass
    def execute(self,value,login_mng):
        match value:
            case "1":
                user_row.change_username(login_mng)
            case "2":
                user_row.change_password(login_mng)
            case "3":
                user_row.delete_account(login_mng)
            case _:
                #user_row.update(login_mng)
                #user_row.create()
                user_row.delete()
                print("\nTato volba není dostupná \n")
    def print_account_options(self,path_to_account_options):
        with open(path_to_account_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")