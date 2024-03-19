import configparser
from src.config.database_connector import DatabaseConnector
from printer.printer import Printer
import getpass

_printer = Printer()
connector =  DatabaseConnector('config/config.ini')

class Login_manager:
    def __init__(self):
        self.username = None
        self.password = None
        self.role = None
        self.role_id = None
        self.loggedIn = False
        self.user_id = None
        
    def login_message(self):
        if self.username != None:
            print(f"Uzivatel : { _printer.print_bold_white(self.username)}")
            print(f"role : {_printer.print_role(self.role)}\n" )
        

    def load_config(self, path_to_config):
        self.config = configparser.ConfigParser()
        self.config.read(path_to_config)
        username = str(self.config.get('DefaultUser', 'username'))
        password = str(self.config.get('DefaultUser', 'password'))
        role_string = str(self.config.get('DefaultUser','role'))
        role_id_for_db = None
        if role_string == "Admin":
            role_id_for_db = 1
        elif role_string == "Manager":
            role_id_for_db = 2
        elif role_string == "Employee":
            role_id_for_db = 3
        else:  
            role_id_for_db = 4

        exist_query = "SELECT COUNT(*) FROM Users WHERE username = %s"
        result = connector.execute_query(exist_query, (username,))
        #If default user already in system
        if result[0][0] == 0:
            query = "INSERT INTO Users (username, password, role_id) VALUES (%s, %s, %s)"
            connector.execute_query_with_commit(query, (username, password, role_id_for_db))

        
        #print("Konfigurace byla načtena")
    def get_role(self):
        return self.role_id
    def isLoggedIn(self):
        return self.loggedIn
    def log_out(self):
        self.loggedIn = False
        self.username = None
        self.password = None
        self.role = None
        self.role_id = None
    def login(self):
        username = input("Zadejte uživatelské jméno: ")
        password = getpass.getpass("Zadejte heslo: ")
        query = "SELECT username, password,role_id,user_id FROM Users WHERE username = %s AND password = %s"
        result = connector.execute_query(query, (username, password))
        #print(result)
        if result:  # Přihlásit uživatele pokud jsou údaje správné
            #Načtení uživatelské role
            if result[0][2] == 1:
                self.role = "Admin"
            elif result[0][2] == 2:
                self.role = "Manager"
            elif result[0][2] == 3:
                self.role = "Employee"
            elif result[0][2] == 4:
                self.role = "Guest"
            self.username = username
            self.password = password
            self.role_id  = result[0][2]
            self.user_id = result[0][3]
            self.loggedIn = True
            print("\nÚspěšně jste se přihlásili!\n")
        else:
            print("\nZadané údaje nebyly správné, nejste přihlášeni.\n")
        
        
        


    