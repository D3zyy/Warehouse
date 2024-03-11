from src.RowGateway.RowGateway_polymorphism.RowGateway  import RowGateway 
from src.validation.validations_methods_user import *


class UserRowGateway(RowGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
        self.user_id = None
        self.password = None
        self.username = None
        self.role_id = None
    def create(self):
        while True:
            username =  validate_name()
            query = "SELECT username from  Users WHERE username = %s"
            result = self.database_connector.execute_query(query, (username,)) 
            if result:
                    print("Uzivatelske jmeno jiz existuje. Zvolte jine jmeno. Zkuste to znovu")

            else:
                password = validate_password()
                while True:
                    role = input("Zadejte roli uzivatele [guest,employee,manager,admin]")
                    match role:
                        case "guest":
                            role = 4
                            break
                        case "employee":
                            role = 3
                            break
                        case "manager":
                            role = 2
                            break
                        case"admin":
                            role = 1
                            break
                        case _:
                            print("Tato role není dostupná. Zkuste to znovu")
                query = "INSERT INTO Users(username,password,role_id)  VALUES(%s,%s,%s)"
                self.database_connector.execute_query_with_commit(query, (username,password,role)) 
                print("\nUspesne jste vytvorili noveho uzivatele!\n")
                break
    def update(self,login_mng):
        while True:
            choice = input("Zadejte atrivut ktery chcete upravit \n 1) uzivatelske jmeno \n 2) heslo \n 3) role\n")
            match choice:
                case "1":
                    self.change_username(login_mng)
                    break
                case "2":
                    self.change_password(login_mng)
                    break
                case "3":
                    while True:
                        role = input("Zadejte roli uzivatele [guest,employee,manager,admin]")
                        match role:
                            case "guest":
                                role = 4
                                break
                            case "employee":
                                role = 3
                                break
                            case "manager":
                                role = 2
                                break
                            case"admin":
                                role = 1
                                break
                            case _:
                                print("Tato role není dostupná. Zkuste to znovu")
                    query = "UPDATE Users SET role_id = %s where user_id = %s "
                    print(f"id uzivatele prihlaseneho : {login_mng.user_id} menime na roli {role}")
                    self.database_connector.execute_query_with_commit(query, (role,login_mng.user_id)) 
                    print("Role byla uspensa zmenena")
                    break

    def delete(self):
        while True:
            username = input("Zadejte uzivatelske jmeno uzivatele ktereho chcete smazat : ")
            query = "SELECT username from  Users WHERE username = %s"
            result = self.database_connector.execute_query(query, (username,)) 
            if result:
                    query = "DELETE FROM  Users where username = %s "
                    self.database_connector.execute_query_with_commit(query, (username,)) 
                    print("Uspense jste smazali uzivatele ze systemu")
                    break
            else:
                print("Toto uzivatelske jmeno neexistuje. Zkuste to znovu")
    def change_username(self,login_mng):
        while True:
            new_name = validate_name()

            query = "SELECT username from  Users WHERE username = %s"
            result = self.database_connector.execute_query(query, (new_name,)) 
            if result:
                print("Uzivatelske jmeno jiz existuje. Zvolte jine jmeno. Zkuste to znovu")

            else:
                query = "UPDATE Users SET username = %s WHERE user_id = %s"
                self.database_connector.execute_query_with_commit(query, (new_name,login_mng.user_id)) 
                login_mng.username = new_name
                print("Uzivatelske jmeno bylo uspesne zmeneno")
                break

    def change_password(self,login_mng):
        while True:
            current_password = input("Zadejte stavajici heslo : ")
            query = "SELECT password from Users where user_id  = %s"
            result = self.database_connector.execute_query(query, (login_mng.user_id,)) 
            if not result[0][0] == current_password:
                print("\nHesla se neshodují! Zkuste to znovu\n")
                
            else: 
                new_password = validate_password()
                query = "UPDATE Users SET password = %s WHERE user_id = %s"
                self.database_connector.execute_query_with_commit(query, (new_password,login_mng.user_id)) 
                login_mng.password = new_password
                print("\nHeslo bylo uspesne zmeneno\n")
                break
    def delete_account(self,login_mng):
        while True:
            confirmation = input(" Jste si jisty ze chcete smazat svuj ucet pro potvrzeni napiste : smazat \n Pro storno napise : storno\n")
            match confirmation:
                case "smazat":
                    query = "DELETE FROM Users WHERE user_id = %s"
                    self.database_connector.execute_query_with_commit(query, (login_mng.user_id,))
                    print("\nUzivatelsky ucet byl uspesne smazan\nByli jste odhlaseni \n")
                    login_mng.log_out()
                    break
                case "storno":
                    print("Smazani uctu bylo stornovano")
                    break
                case _:
                    print("Volba není platná akce byla stornovana")
                    break






        

        