import json 
from src.config.database_connector import DatabaseConnector
from src.RowGateway.UserRowGateway import UserRowGateway
from printer.printer import Printer
from src.TableGateway.UsersTableGateway import UserTableGateway
from src.validation.validations_methods_admin import *


_printer = Printer()
connector =  DatabaseConnector('config/config.ini')
user_row = UserRowGateway(connector)
user_table = UserTableGateway(connector)

class admin_manager:
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
                user_table.get_all_users()
            case "5":
                    confirmation = input(" Jste si jisty ze chcete smazat vsechny data ze systemu pro potvrzeni napiste : smazat \n Pro storno napise : storno\n")
                    match confirmation:
                        case "smazat":
                            tables_to_delete = ["Purchases", "Sales", "Products", "Categories", "Users", "Suppliers", "Customers", "Roles","Addresses"]
                            
                            for table in tables_to_delete:
                                query = f"DELETE FROM {table}"
                                query_auto_increamaent = f"ALTER TABLE {table} AUTO_INCREMENT = 1;"
                                connector.execute_query_with_commit(query)
                                connector.execute_query_with_commit(query_auto_increamaent)
                            
                            
                            print("\nVšechna data byla úspěšně smazána\n")
                            login_mng.log_out()
                        case "storno":
                              print("\Smazani dat  bylo stornovano\n")
                        case _:
                            print("Volba není platná akce byla stornovana")
            case "6":
                confirmation = input(" Jste si jisty ze chcete vlozit testovaci data do systemu pro potvrzeni napiste : vlozit \n Pro storno napise : storno\n")
                match confirmation:
                        case "vlozit":
                                self.insert_sample_data()
                        case "storno":
                              print("\Vklad  dat  byl stornovan\n")
                        case _:
                            print("Volba není platná akce byla stornovana")
                
            case "7":
                confirmation = input(" Jste si jisty ze chcete obnovit cely system do tovarniho nastaveni vcetne dat pro potvrzeni napiste : obnoveni \n Pro storno napise : storno\n Obnoveni muze trvat delsi dobu. \n")
                
                match confirmation:
                    case "obnoveni":
                        drop_table_queries = [
                            "DROP TABLE IF EXISTS Purchases;",
                            "DROP TABLE IF EXISTS Sales;",
                            "DROP TABLE IF EXISTS Products;",
                            "DROP TABLE IF EXISTS Suppliers;",
                            "DROP TABLE IF EXISTS Customers;",
                            "DROP TABLE IF EXISTS Addresses;",
                            "DROP TABLE IF EXISTS Categories;",
                            "DROP TABLE IF EXISTS Users;",
                            "DROP TABLE IF EXISTS Roles;"
                        ]

                        for drop_query in drop_table_queries:
                            connector.execute_query_with_commit(drop_query)
                        table_definitions = [
                            """
                            CREATE TABLE Categories (
                                category_id INT AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(50) NOT NULL
                            )
                            """,
                            """
                            CREATE TABLE Products (
                                product_id INT AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(100) NOT NULL,
                                category_id INT,
                                price DECIMAL(10,2) NOT NULL,
                                quantity INT NOT NULL CHECK (quantity >= 0),
                                FOREIGN KEY (category_id) REFERENCES Categories(category_id)
                            )
                            """,
                            """
                            CREATE TABLE Addresses (
                                address_id INT AUTO_INCREMENT PRIMARY KEY,
                                street VARCHAR(255) NOT NULL,
                                city VARCHAR(100) NOT NULL,
                                postal_code VARCHAR(20) NOT NULL
                            )
                            
                            """,
                            """
                            CREATE TABLE Customers (
                                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(100) NOT NULL,
                                address_id INT NOT NULL,
                                contact_number VARCHAR(20) NOT NULL,
                                FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
                            )
                            """,
                            """
                            CREATE TABLE Suppliers (
                                supplier_id INT AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(100) NOT NULL,
                                address_id INT NOT NULL,
                                contact_number VARCHAR(20) NOT NULL,
                                FOREIGN KEY (address_id) REFERENCES Addresses(address_id)
                            )
                            """,
                            """
                            CREATE TABLE Purchases (
                                purchase_id INT AUTO_INCREMENT PRIMARY KEY,
                                product_id INT,
                                supplier_id INT,
                                quantity INT NOT NULL CHECK (quantity >= 0),
                                price DECIMAL(10,2) NOT NULL CHECK (price > 0),
                                date DATE NOT NULL,
                                FOREIGN KEY (product_id) REFERENCES Products(product_id),
                                FOREIGN KEY (supplier_id) REFERENCES Suppliers(supplier_id)
                            )
                            """,
                            """
                            CREATE TABLE Sales (
                                sale_id INT AUTO_INCREMENT PRIMARY KEY,
                                product_id INT,
                                customer_id INT,
                                quantity INT NOT NULL CHECK (quantity >= 0),
                                price DECIMAL(10,2) NOT NULL CHECK (price > 0),
                                date DATE NOT NULL,
                                FOREIGN KEY (product_id) REFERENCES Products(product_id),
                                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
                            )
                            """,
                            """
                            CREATE TABLE Roles (
                                role_id INT AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(50) NOT NULL
                            )
                            """,
                            """
                            CREATE TABLE Users (
                                user_id INT AUTO_INCREMENT PRIMARY KEY,
                                username VARCHAR(50) NOT NULL,
                                password VARCHAR(255) NOT NULL,
                                role_id INT NOT NULL,
                                FOREIGN KEY (role_id) REFERENCES Roles(role_id)
                            )
                            """
                        ]

                        for definition in table_definitions:
                            connector.execute_query_with_commit(definition)
                        self.insert_sample_data()
                        print("\nCely system byl obnoven do tovarniho nastaveni\n")
                        login_mng.log_out()
                    case "storno":
                        print("\Obnoveni  bylo stornovano\n")
                    
                    case _:
                          print("Volba není platná akce byla stornovana")
            case "8":
                chose_which_part = input("Vyberte kategorii kterou chcete upravit : \n 1) Databaze \n 2) Zakladni uzivatel  \n 3) Jmeno skladu\n ")
                match chose_which_part:
                     case "1":
                          chose_which_part = input("Vyberte cast kterou chcete upravit : \n 1) host \n 2) uzivatel  \n 3) heslo \n 4) databaze \n ")
                          match chose_which_part:
                               case "1":
                                     print(f"soucasny host : {connector.config.get('Database', 'host')}")
                                     connector.config['Database']['host'] = validate_domain()
                                     with open('config/config.ini', 'w') as configfile:
                                        connector.config.write(configfile)
                                     print(f"novy host databaze : {connector.config.get('Database', 'host')}")
                                    
                               case "2":
                                    print(f"soucasny uzivatel : {connector.config.get('Database', 'user')}")
                                    connector.config['Database']['user'] = validate_username_db()
                                    with open('config/config.ini', 'w') as configfile:
                                        connector.config.write(configfile)
                                    print(f"novy uzivatel databaze : {connector.config.get('Database', 'user')}")
                               case "3":
                                    print(f"soucasne heslo : {connector.config.get('Database', 'password')}")
                                    connector.config['Database']['password'] = input("Zadejte heslo :")
                                    with open('config/config.ini', 'w') as configfile:
                                        connector.config.write(configfile)
                                    print(f"nove heslo databaze : {connector.config.get('Database', 'password')}")
                               case "4":
                                    print(f"soucasna databaze : {connector.config.get('Database', 'database')}")
                                    connector.config['Database']['database'] = validate_database_name()
                                    with open('config/config.ini', 'w') as configfile:
                                        connector.config.write(configfile)
                                    print(f"nova databaze : {connector.config.get('Database', 'database')}")
                               case _:
                                     print("Tato volba není platná ")
                     case "2":
                          chose_which_part = input("Vyberte cast kterou chcete upravit : \n 1) jmeno \n 2) heslo  \n 3) role  \n ")
                          match chose_which_part:
                               case "1":
                                    print(f"soucasny jmeno uzivatele : {connector.config.get('DefaultUser', 'username')}")
                                    connector.config['DefaultUser']['username'] = validate_database_name()
                                    with open('config/config.ini', 'w') as configfile:
                                        connector.config.write(configfile)
                                    print(f"novy jmeno uzivatele  : {connector.config.get('DefaultUser', 'role')}")
                               case "2":
                                    print(f"soucasne heslo : {connector.config.get('DefaultUser', 'password')}")
                                    connector.config['DefaultUser']['password'] = validate_password()
                                    with open('config/config.ini', 'w') as configfile:
                                        connector.config.write(configfile)
                                    print(f"nove heslo uzivatele  : {connector.config.get('DefaultUser', 'password')}")
                               case "3":
                                    print(f"soucasna role : {connector.config.get('DefaultUser', 'role')}")
                                    connector.config['DefaultUser']['role'] = validate_role()
                                    with open('config/config.ini', 'w') as configfile:
                                        connector.config.write(configfile)
                                    print(f"nova role uzivatele  : {connector.config.get('DefaultUser', 'role')}")
                               case _:
                                     print("Tato volba není platná  ")
                     case "3":
                           print(f"soucasny nazev skladu : {connector.config.get('Warehouse', 'name')}")
                           connector.config['Warehouse']['name'] = validate_username_db()
                           with open('config/config.ini', 'w') as configfile:
                                 connector.config.write(configfile)
                           print(f"novy nazev skladu  : {connector.config.get('Warehouse', 'name')}")
                     case _:
                          print("Tato volba není platná ")


                
            
            case _:
                print("\nTato volba není dostupná \n")
    def print_admin_options(self,path_to_manager_options):
        _printer.print_admin_section()
        with open(path_to_manager_options) as json_file:
            options_from_json = json.load(json_file)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")
    def insert_sample_data(self):
                        insert_queries = [
                            "INSERT INTO Categories (name) VALUES "
                            "('Elektronika'), "
                            "('Oblečení'), "
                            "('Kuchyňské potřeby'), "
                            "('Domácí spotřebiče'), "
                            "('Sportovní vybavení');",

                            "INSERT INTO Addresses (street, city, postal_code) VALUES "
                            "('Hlavní 123', 'Praha', '110 00'), "
                            "('Ulice 456', 'Brno', '602 00'), "
                            "('Náměstí 789', 'Ostrava', '700 00'), "
                            "('Příkladná 12', 'Plzeň', '301 00'), "
                            "('Sportovní 24', 'Liberec', '460 00'), "
                            "('Parková 7', 'České Budějovice', '370 01'), "
                            "('Zahrádkářská 15', 'Olomouc', '779 00'), "
                            "('Lesní 3', 'Hradec Králové', '500 09'), "
                            "('Vinohradská 88', 'Ústí nad Labem', '400 01'), "
                            "('Školní 50', 'Karlovy Vary', '360 05'), "
                            "('Jedovnická 2', 'Zlín', '760 01'), "
                            "('Purkyňova 30', 'Jihlava', '586 01'), "
                            "('Sokolovská 17', 'Pardubice', '532 01'), "
                            "('Masarykovo náměstí 1', 'Teplice', '415 01'), "
                            "('Smetanova 5', 'Děčín', '405 02');",

                            "INSERT INTO Products (name, category_id, price, quantity) VALUES "
                            "('Televize Samsung 50\" 4K', 1, 9999.99, 10), "
                            "('Dámský kabát zimní', 2, 1299.50, 20), "
                            "('Kávovar Philips HD8827/09', 3, 1499.00, 15), "
                            "('Mikrovlnná trouba Bosch', 4, 899.99, 12), "
                            "('Posilovací lavice York', 5, 399.99, 8);",

                            "INSERT INTO Suppliers (name, address_id, contact_number) VALUES "
                            "('ElektroWorld s.r.o.', 1, '+420 123 456 789'), "
                            "('Modní trendy spol. s.r.o.', 2, '+420 987 654 321'), "
                            "('Kuchyňské potřeby a.s.', 3, '+420 111 222 333'), "
                            "('Domácí spotřebiče CZ', 4, '+420 444 555 666'), "
                            "('Sportovní vybavení Plus', 5, '+420 777 888 999');",

                            "INSERT INTO Customers (name, address_id, contact_number) VALUES "
                            "('Jan Novák', 6, '+420 111 222 333'), "
                            "('Marie Kovářová', 7, '+420 444 555 666'), "
                            "('Petr Dvořák', 8, '+420 777 888 999'), "
                            "('Eva Procházková', 9, '+420 987 654 321'), "
                            "('Tomáš Svoboda', 10, '+420 123 456 789');",

                            "INSERT INTO Purchases (product_id, supplier_id, quantity, price, date) VALUES "
                            "(1, 1, 5, 8999.99, '2024-03-01'), "
                            "(2, 2, 10, 1200.50, '2024-03-02'), "
                            "(3, 3, 8, 1399.00, '2024-03-03'), "
                            "(4, 4, 6, 850.99, '2024-03-04'), "
                            "(5, 5, 3, 349.99, '2024-03-05');",

                            "INSERT INTO Sales (product_id, customer_id, quantity, price, date) VALUES "
                            "(1, 1, 1, 9999.99, '2024-03-01'), "
                            "(2, 2, 2, 1299.50, '2024-03-02'), "
                            "(3, 3, 1, 1499.00, '2024-03-03'), "
                            "(4, 4, 2, 899.99, '2024-03-04'), "
                            "(5, 5, 1, 399.99, '2024-03-05');",

                            "INSERT INTO Roles (name) VALUES "
                            "('Admin'), "
                            "('Manager'), "
                            "('Employee'), "
                            "('Guest');",

                            "INSERT INTO Users (username, password, role_id) VALUES "
                            "('admin', 'admin', 1), "
                            "('manager', 'manager', 2), "
                            "('employee', 'employee', 3), "
                            "('guest', 'guest', 4);"
                        ]

                        for query in insert_queries:
                            connector.execute_query_with_commit(query)
                        print("\nData byla uspesne naimportovana\n")