from src.menu_manager.supplier_manager import supplier_manager
from src.menu_manager.customer_manager  import customer_manager
from src.menu_manager.sale_manager import sale_manager
import json

options = {}
supplier_mng = supplier_manager()
customer_mng = customer_manager()
sale_mng = sale_manager()

class Guest_role:
    def __init__(self):
        pass
    def select_option_guest(self,login_mng):
        choice = str(input())
        match choice:
            case "1":
                supplier_mng.print_supplier_options('menu_manager/options_section_json/options_supplier.json')
                choice = str(input())
                supplier_mng.execute(choice)   
            case "2":
                customer_mng.print_customer_options('menu_manager/options_section_json/options_customer.json')
                choice = str(input())
                customer_mng.execute(choice)
            case "3":
                sale_mng.print_sale_options('menu_manager/options_section_json/options_sale.json')
                choice = str(input()) 
                sale_mng.execute(choice)
            case "4":
                    login_mng.login()
            case "5":
                    print(5)
            case _:
                print("\nTato volba není dostupná\n")
    def print_options_guest(self,path_to_guest_option_json):
        with open(path_to_guest_option_json) as json_file:
            options_from_json = json.load(json_file)
            options.update(options_from_json)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")