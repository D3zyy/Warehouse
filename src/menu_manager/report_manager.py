import json 
from src.RowGateway.SaleRowGateway import SaleRowGateway
from src.TableGateway.SalesTableGateway import SaleTableGateway
from src.config.database_connector import DatabaseConnector
from src.TableGateway.UsersTableGateway import UserTableGateway
from src.TableGateway.RolesTableGateway import RoleTableGateway
from src.TableGateway.ProductsTableGateway import ProductTableGateway
from src.TableGateway.CategoriesTableGateway import CategoryTableGateway
from src.TableGateway.AddressesTableGateway import AddressesTableGateway
from src.TableGateway.CustomerTableGateway import CustomerTableGateway
from src.TableGateway.SupplierTableGateway import SupplierTableGateway
from src.TableGateway.PurchaseTableGateway import PurchaseTableGateway
from src.TableGateway.SalesTableGateway import SaleTableGateway

connector =  DatabaseConnector('config/config.ini')
sale_row = SaleRowGateway(connector)
sale_table = SaleTableGateway(connector)
user_table = UserTableGateway(connector)
role_table = RoleTableGateway(connector)
product_table = ProductTableGateway(connector)
category_table = CategoryTableGateway(connector)
address_table = AddressesTableGateway(connector)
customer_table = CustomerTableGateway(connector)
supplier_table = SupplierTableGateway(connector)
purchase_table = PurchaseTableGateway(connector)
sale_table = SaleTableGateway(connector)


class report_manager:
    def __init__(self):
        pass
    def execute(self,value,role_id):
        match value:
            case "1":
                if role_id == 1 or role_id == 2:
                    choice = input(" 1) Vypsat vsechny uzivatele\n 2) Vypsat vsechny uzivatele role guest\n 3) vypsat vsechny uzivatele role employee\n 4) vypsat vsechny uzivatele role manager\n 5) vypsat vsechny uzivatele role admin \n")
                    match choice:
                        case "1":
                            user_table.get_all_users()
                        case "2":
                            user_table.get_all_guest_users()
                        case "3":
                            user_table.get_all_employee_users()
                        case"4":
                            user_table.get_all_manager_users()
                        case "5":
                            user_table.get_all_admin_users()
                        case _:
                            print("Tato volba neni dostupna")
                else:
                    print("Pristup odepren")
            case "2":
                if role_id == 1 or role_id == 2:
                    choice = input(" 1) Vypsat vsechny role\n")
                    match choice:
                        case "1":
                            role_table.get_all_roles()
                        case _:
                            print("Tato volba neni dostupna")
                else:
                    print("Pristup odepren")
            case "3":
                if role_id == 1 or role_id == 2:
                    choice = input(" 1) Vypsat vsechny produkty\n 2) Vypsat produkt ktereho je na sklade nejvice\n 3) vypsat produkt ktereho je na sklade nejmene \n 4) vypsat nejdrazsi produkt na sklade \n 5) vypsat nejlevnejsi produkt na sklade\n")
                    match choice:
                        case "1":
                            product_table.get_all_products()
                        case "2":
                            product_table.get_product_that_we_have_the_most()
                        case "3":
                            product_table.get_product_that_we_have_the_less()
                        case"4":
                            product_table.get_product_highest_price()
                        case "5":
                            product_table.get_product_lowest_price()
                        case _:
                            print("Tato volba neni dostupna")
                else:
                    print("Pristup odepren")
            case "4":
                if role_id == 1 or role_id == 2:
                    choice = input(" 1) Vypsat vsechny kategorie produktu\n")
                    match choice:
                        case "1":
                            category_table.get_all_categories()
                        case _:
                            print("Tato volba neni dostupna")
                else:
                    print("Pristup odepren")
            case "5":
                if role_id == 1 or role_id == 2:
                    choice = input(" 1) Vypsat vsechny adresy \n 2) Vypsat pocet adres podle mesta\n 3) Vypsat pocet adres podle PSC\n 4) Vypsat mesto s nejvice adresami")
                    match choice:
                        case "1":
                            address_table.get_all_addresses()
                        case "2":
                            address_table.get_number_of_address_by_city()
                        case "3":
                            address_table.get_number_of_address_by_psc()
                        case "4":
                            address_table.get_highest_city_with_addresses()
                        case _:
                            print("Tato volba neni dostupna")
                else:
                    print("Pristup odepren")
            case "6":
                if role_id == 1 or role_id == 2:
                    choice = input(" 1) Vypsat vsechny zakazniky \n")
                    match choice:
                        case "1":
                            customer_table.get_all_customers()
                        case _:
                            print("Tato volba neni dostupna")
                else:
                    print("Pristup odepren")
            case "7":
                if role_id == 1 or role_id == 2:
                    choice = input(" 1) Vypsat vsechny dodavatele \n")
                    match choice:
                        case "1":
                            supplier_table.get_all_suppliers()
                        case _:
                            print("Tato volba neni dostupna")
                else:
                    print("Pristup odepren")
            case "8":
                if role_id == 1 or role_id == 2:
                    choice = input(" 1) Vypsat vsechny prijemky \n 2) Vypsat specifickou prijemku")
                    match choice:
                        case "1":
                            purchase_table.get_all_purchases()
                        case "2":
                            purchase_table.get_specific_purchase()
                        case _:
                            print("Tato volba neni dostupna")
                else:
                    print("Pristup odepren")
            case "9":
                if role_id == 1 or role_id == 2:
                    choice = input(" 1) Vypsat vsechny vydejky \n 2) Vypsat specifickou vydejku")
                    match choice:
                        case "1":
                            sale_table.get_all_sales()
                        case "2":
                            sale_table.get_specific_sale()
                        case _:
                            print("Tato volba neni dostupna")
                else:
                    print("Pristup odepren")
                print("Vydejky")
            case _:
                print("\nTato volba není dostupná \n")
    def print_report_options(self,path_to_sale_options):
        with open(path_to_sale_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")