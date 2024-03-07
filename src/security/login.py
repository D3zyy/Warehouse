import configparser
from src.config.database_connector import DatabaseConnector
connector =  DatabaseConnector('config/config.ini')

class Login_manager:
    def __init__(self):
        self.username = None
        self.password = None
        self.role = None
        self.loggedIn = False
        
    def login_message(self):
        if self.username != None:
            print(f"Přihlášen jako :  {self.username} Role : {self.role} \n ")
        else:
            print(f"Přihlášen jako GUEST")

    def load_config(self, path_to_config):
        self.config = configparser.ConfigParser()
        self.config.read(path_to_config)
        username = str(self.config.get('DefaultUser', 'username'))
        password = str(self.config.get('DefaultUser', 'password'))
        role_string = str(self.config.get('DefaultUser','role'))
        
        if role_string == "Admin":
            role_id = 1
        elif role_string == "Manager":
            role_id = 2
        elif role_string == "Employee":
            role_id = 3
        else:  
            role_id = 4
        
        query = "INSERT INTO Users (username, password, role_id) VALUES (%s, %s, %s)"  
        connector.execute_query(query, (username, password, role_id))
        
        print("Konfigurace byla načtena")


    def isLoggedIn(self):
        return self.loggedIn
    def login(self,username,password):
       if username == self.username and password == self.password:
           self.load_config = True
           print("Uspěšně jste se přihlásily!")
       else:
            print("Zadané údaje nebyli správné, nebyli jste přihlášeny")

    