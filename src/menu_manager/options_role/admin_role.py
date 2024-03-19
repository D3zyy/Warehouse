from src.menu_manager.supplier_manager import supplier_manager
from src.menu_manager.customer_manager  import customer_manager
from src.menu_manager.sale_manager import sale_manager
from src.menu_manager.account_manager import account_manager
from src.menu_manager.admin_manager import admin_manager
from src.menu_manager.warehouse_manager import warehouse_manager
from src.menu_manager.purchases_manager import purchase_manager
import json


supplier_mng = supplier_manager()
customer_mng = customer_manager()
sale_mng = sale_manager()
account_mng = account_manager()
admin_mng = admin_manager()
warehouse_mng = warehouse_manager()
purchase_mng = purchase_manager()

class Admin_role:
    def __init__(self):
        pass
    def select_option_admin(self,login_mng,role_id):
        choice = str(input())
        match choice:
            case "1":
                purchase_mng.print_purchase_options('menu_manager/options_section_json/options_purchase.json')
                choice = str(input()) 
                purchase_mng.execute(choice,role_id) 
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
                warehouse_mng.print_warehouse_options('menu_manager/options_section_json/options_warehouse.json')
                choice = str(input())
                warehouse_mng.execute(choice,role_id)
            case"6":
                  admin_mng.print_admin_options('menu_manager/options_section_json/options_admin.json')
                  choice = str(input())
                  admin_mng.execute(choice,login_mng)
            case"7":
                  print("generovat reporty")
            case "8":
                  account_mng.print_account_options('menu_manager/options_section_json/options_account.json')
                  choice = str(input())
                  account_mng.execute(choice,login_mng)
            case "9":
               login_mng.log_out()
            case "10":
                exit()
            case _:
                print("\nTato volba není dostupná\n")
    def print_options_admin(self,path_to_guest_option_json):
        with open(path_to_guest_option_json) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")