from src.config.Initialization import Settings
import json
from src.menu_manager.supplier_manager import supplier_manager
from src.menu_manager.customer_manager  import customer_manager
from src.menu_manager.sale_manager import sale_manager



supplier_mng = supplier_manager()
customer_mng = customer_manager()
sale_mng = sale_manager()


#Cesta uvedena relativně kde je importován menu_options v main.py
settings1 = Settings('config/config.ini')

options = {}

class Options_manager:
    def __init__(self) -> None:
        pass
    def print_options_by_role(self,role_id):
        if role_id == 1:
            self.print_options_admin('menu_manager/options_role_json/options_role_admin.json')
        elif role_id == 2:
             self.print_options_manager('menu_manager/options_role_json/options_role_manager.json')
        elif role_id == 3:
             self.print_options_employee('menu_manager/options_role_json/options_role_employee.json')
        elif role_id == 4:
               self.print_options_guest('menu_manager/options_role_json/options_role_manager.json')
      
    def print_options_guest(self,path_to_guest_option_json):
        with open(path_to_guest_option_json) as json_file:
            options_from_json = json.load(json_file)
            options.update(options_from_json)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")
    def print_options_employee(self,path_to_employee_option_json):
        with open(path_to_employee_option_json) as json_file:
            options_from_json = json.load(json_file)
            options.update(options_from_json)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")
    def print_options_manager(self,path_to_manager_option_json):
        with open(path_to_manager_option_json) as json_file:
            options_from_json = json.load(json_file)
            options.update(options_from_json)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")
    def print_options_admin(self,path_to_admin_option_json):
        with open(path_to_admin_option_json) as json_file:
            options_from_json = json.load(json_file)
            options.update(options_from_json)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")
    def welcome_message(self):
        print(f"Vítejte v {settings1.warehouse_name} \n")
    def select_option(self,role):
        choice = str(input())
        match choice:
            case "1":
                supplier_mng.print_supplier_options('menu_manager/options_supplier.json')
                choice = str(input())
                supplier_mng.execute(choice)   
            case "2":
                customer_mng.print_customer_options('menu_manager/options_customer.json')
                choice = str(input())
                customer_mng.execute(choice)
            case "3":
                sale_mng.print_sale_options('menu_manager/options_sale.json')
                choice = str(input()) 
                sale_mng.execute(choice)
            case "4":
                    print(4)
            case "5":
                    print(5)
            case _:
                print("\nTato volba není dostupná\n")
        #print(f"funguje : {options}")



#welcome_message()
##print_options('options.json')
