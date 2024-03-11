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
        pass
    def update(self):
        pass
    def delete(self,password):
        pass
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
                print("\nHesla se neshodují!\n")
                break
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
                    print("\nUzivatelsky ucet byl uspesne smazan\n Byli jste odhlaseni \n")
                    login_mng.log_out()
                    break
                case "storno":
                    print("Smazani uctu bylo stornovano")
                    break
                case _:
                    print("Volba není platná akce byla stornovana")
                    break






        

        