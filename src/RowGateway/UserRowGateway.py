from src.RowGateway.RowGateway_polymorphism.RowGateway  import RowGateway 
from src.validation.validations_methods_user import *


class UserRowGateway(RowGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
        self.user_id = None
        self.password = None
        self.username = None
        self.role_id = None
    def create(self,login_mng):
        while True:
            username =  validate_name()
            query = "SELECT username from  Users WHERE username = %s"
            result = self.database_connector.execute_query(query, (username,)) 
            if result:
                    print("Uzivatelske jmeno jiz existuje. Zvolte jine jmeno. Zkuste to znovu")

            else:
                password = validate_password()
                while True:
                    if login_mng.role == "Admin":
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
                    elif login_mng.role =="Manager":
                        role = input("Zadejte roli uzivatele [guest,employee,manager]")
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
                    while True:
                        username = str(input("Zadejte uzivatelske jmeno uzivatele kteremu chcete zmenit uzivatelske jmeno : "))
                        #Check role
                        query_role = "SELECT Roles.name FROM Users INNER JOIN Roles ON Users.role_id = Roles.role_id WHERE Users.username= %s;"
                        result = self.database_connector.execute_query(query_role, (username,))
                        if result:
                            role_of_editing_user = result[0][0]
                            if login_mng.role == role_of_editing_user:
                                print("Mate povoleni editovat tohoto uzivatele")
                            elif login_mng.role == "Manager" and role_of_editing_user == "Guest" or role_of_editing_user == "Employee":
                                print("Mate povoleni editovat tohoto uzivatele")
                            elif login_mng.role == "Admin" and role_of_editing_user == "Manager" or role_of_editing_user == "Employee" or role_of_editing_user == "Guest":
                                print("Mate povoleni editovat tohoto uzivatele")
                            else:
                                print("Nemáte opravneni editovat tohoto uzivatele")
                                break
                        query = "SELECT username from  Users WHERE username = %s"
                        result = self.database_connector.execute_query(query, (username,)) 
                        if result:
                                while True:
                                    new_name = validate_name()

                                    query = "SELECT username from  Users WHERE username = %s"
                                    result = self.database_connector.execute_query(query, (new_name,)) 
                                    if result:
                                        print("Uzivatelske jmeno jiz existuje. Zvolte jine jmeno. Zkuste to znovu")

                                    else:
                                        query = "UPDATE Users SET username = %s WHERE username = %s"
                                        self.database_connector.execute_query_with_commit(query, (new_name,username)) 
                                        print("Uspense jste upravili uzivatelske jmeno v systemu")
                                        break


                                
                        else:
                            print("Toto uzivatelske jmeno v systemu neexistuje. Zkuste to znovu")
                        break
                            
                            
                    break
                case "2":
                    while True:
                        username = str(input("Zadejte uzivatelske jmeno uzivatele kteremu chcete zmenit heslo  : "))
                        #Check role
                        query_role = "SELECT Roles.name FROM Users INNER JOIN Roles ON Users.role_id = Roles.role_id WHERE Users.username= %s;"
                        result = self.database_connector.execute_query(query_role, (username,))
                        if result:
                            role_of_editing_user = result[0][0]
                            if login_mng.role == role_of_editing_user:
                                print("Mate povoleni editovat tohoto uzivatele")
                            elif login_mng.role == "Manager" and role_of_editing_user == "Guest" or role_of_editing_user == "Employee":
                                print("Mate povoleni editovat tohoto uzivatele")
                            elif login_mng.role == "Admin" and role_of_editing_user == "Manager" or role_of_editing_user == "Employee" or role_of_editing_user == "Guest":
                                print("Mate povoleni editovat tohoto uzivatele")
                            else:
                                print("Nemáte opravneni editovat tohoto uzivatele")
                                break


                        query = "SELECT username from  Users WHERE username = %s"
                        result = self.database_connector.execute_query(query, (username,)) 
                        if result:
                            new_password = validate_password()
                            query = "UPDATE Users SET password = %s WHERE username = %s"
                            self.database_connector.execute_query_with_commit(query, (new_password,username)) 
                            login_mng.password = new_password
                            print("\nHeslo bylo uspesne zmeneno\n")
                            break
                        else: 
                            print("Uzivatel s timto jmenem nebyl v systemu nalezen. Zkuste to znovu")                   
                    break
                case "3":
                    while True:
                        username_of_account  = str(input("Zadejte uzivatelske jmeno uctu ktery chcete upravit : "))
                        #Check role
                        query_role = "SELECT Roles.name FROM Users INNER JOIN Roles ON Users.role_id = Roles.role_id WHERE Users.username= %s;"
                        result = self.database_connector.execute_query(query_role, (username_of_account,))
                        if result:
                            role_of_editing_user = result[0][0]
                            if login_mng.role == role_of_editing_user:
                                print("Mate povoleni editovat tohoto uzivatele")
                            elif login_mng.role == "Manager" and role_of_editing_user == "Guest" or role_of_editing_user == "Employee":
                                print("Mate povoleni editovat tohoto uzivatele")
                            elif login_mng.role == "Admin" and role_of_editing_user == "Manager" or role_of_editing_user == "Employee" or role_of_editing_user == "Guest":
                                print("Mate povoleni editovat tohoto uzivatele")
                            else:
                                print("Nemáte opravneni editovat tohoto uzivatele")
                                break

                            
                        #Check existance
                        query = "SELECT username from  Users WHERE username = %s"
                        result = self.database_connector.execute_query(query, (username_of_account,)) 
                        if result:
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
                            query = "UPDATE Users SET role_id = %s where username = %s "
                            #print(f"username uzivatele  : {username_of_account} menime na roli {role}")
                            self.database_connector.execute_query_with_commit(query, (role,username_of_account)) 
                            print("\nRole byla uspesne zmenena\n")
                            break                             

                        else:
                            print("Toto uzivatelske jmeno v systemu neexistuje")    
            break

                        
                        

    def delete(self,login_mng):
        while True:
            username = str(input("Zadejte uzivatelske jmeno uzivatele ktereho chcete smazat : "))
            query_role = "SELECT Roles.name FROM Users INNER JOIN Roles ON Users.role_id = Roles.role_id WHERE Users.username= %s;"
            result = self.database_connector.execute_query(query_role, (username,))
            if result:
                    role_of_editing_user = result[0][0]
                    if login_mng.role == role_of_editing_user:
                         print("Mate povoleni smazat tohoto uzivatele")
                    elif login_mng.role == "Manager" and role_of_editing_user == "Guest" or role_of_editing_user == "Employee":
                          print("Mate povoleni smazat tohoto uzivatele")
                    elif login_mng.role == "Admin" and role_of_editing_user == "Manager" or role_of_editing_user == "Employee" or role_of_editing_user == "Guest":
                          print("Mate povoleni smazat tohoto uzivatele")
                    else:
                          print("Nemáte opravneni smazat tohoto uzivatele")
                          break


            query = "SELECT username from  Users WHERE username = %s"
            result = self.database_connector.execute_query(query, (username,)) 
            if result:
                    query = "DELETE FROM  Users where username = %s "
                    self.database_connector.execute_query_with_commit(query, (username,)) 
                    print("Uspense jste smazali uzivatele ze systemu")
                    break
            else:
                print("Toto uzivatelske jmeno v systemu neexistuje. Zkuste to znovu")
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






        

        