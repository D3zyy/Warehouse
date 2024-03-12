from src.menu_manager.supplier_manager import supplier_manager
from src.menu_manager.customer_manager  import customer_manager
from src.menu_manager.sale_manager import sale_manager
from src.menu_manager.account_manager import account_manager
from src.menu_manager.admin_manager import admin_manager
import json


supplier_mng = supplier_manager()
customer_mng = customer_manager()
sale_mng = sale_manager()
account_mng = account_manager()
admin_mng = admin_manager()

class Admin_role:
    def __init__(self):
        pass
    def select_option_admin(self,login_mng,role_id):
        choice = str(input())
        match choice:
            case "1":
                print("Prijemky soon")   
            case "2":
                sale_mng.print_sale_options('menu_manager/options_section_json/options_sale.json')
                choice = str(input()) 
                sale_mng.execute(choice,role_id)
            case "3":
                customer_mng.print_customer_options('menu_manager/options_section_json/options_customer.json')
                choice = str(input())
                customer_mng.execute(choice,role_id)
            case "4":
                supplier_mng.print_supplier_options('menu_manager/options_section_json/options_supplier.json')
                choice = str(input())
                supplier_mng.execute(choice,role_id)
            case "5":
                    print("Sklad sekce soon")      
            case"6":
                  admin_mng.print_manager_options('menu_manager/options_section_json/options_admin.json')
                  choice = str(input())
                  admin_mng.execute(choice,login_mng)
            case"7":
                  account_mng.print_account_options('menu_manager/options_section_json/options_account.json')
                  choice = str(input())
                  account_mng.execute(choice,login_mng)
            case "8":
                  login_mng.log_out()
            case "9":
                  exit()
            case _:
                print("\nTato volba není dostupná\n")
    def print_options_admin(self,path_to_guest_option_json):
        with open(path_to_guest_option_json) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")