from src.menu_manager.supplier_manager import supplier_manager
from src.menu_manager.customer_manager  import customer_manager
from src.menu_manager.sale_manager import sale_manager
import json


supplier_mng = supplier_manager()
customer_mng = customer_manager()
sale_mng = sale_manager()

class Employee_role:
    def __init__(self):
        pass
    def select_option_employee(self,login_mng,role_id):
        choice = str(input())
        match choice:
            case "1":
                   print("vydejky soon")
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
                    print("sklad sekce soon")
            case "6":
                    print("Muj ucet soon")
            case "7":
                  login_mng.log_out()
            case "8":
                  exit()
            case _:
                print("\nTato volba není dostupná\n")
    def print_options_employee(self,path_to_employee_option_json):
        with open(path_to_employee_option_json) as json_file:
            options_from_json = json.load(json_file)
            
            for key, value in options_from_json.items():
                print(f"{key}) {value}")