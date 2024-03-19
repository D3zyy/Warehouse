from src.TableGateway.TableGateway_polymorphism.TableGateway  import TableGateway 
from src.validation.validations_methods_user import *


class UserTableGateway(TableGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
    def get_all_users(self):
        print("\n")
        query = "SELECT Users.user_id,Users.username,Users.password,Roles.name FROM Users inner join Roles on Roles.role_id = Users.role_id"
        rows = self.database_connector.execute_query(query)
        print("Uzivatele systemu:")
        print("{:<5} {:<20} {:<20} {:<5}".format("ID", "Uzivatelske jmeno","heslo","Role"))
        print("-" * 60)
        for row in rows:
            print("{:<5} {:<20} {:<20} {:<5}".format(row[0], row[1] ,row[2], row[3]))
        print("\n")
    def get_specific_user(self,login_mng):
            privilages = False
            username = check_existance_of_user(self.database_connector)
            #Check role
            query_role = "SELECT Roles.name FROM Users INNER JOIN Roles ON Users.role_id = Roles.role_id WHERE Users.username= %s;"
            result = self.database_connector.execute_query(query_role, (username,))
            if result:
                   role_of_printing_user = result[0][0]
                   if login_mng.role == role_of_printing_user:
                            privilages = True
                   elif login_mng.role == "Manager" and role_of_printing_user == "Guest" or role_of_printing_user == "Employee":
                            privilages = True
                   elif login_mng.role == "Admin" and role_of_printing_user == "Manager" or role_of_printing_user == "Employee" or role_of_printing_user == "Guest":
                             privilages = True
                   else:
                        print("\nNemáte opravneni zobrazit tohoto uzivatele\n")           
            if privilages == True:
                query = "SELECT Users.user_id,Users.username,Users.password,Roles.name FROM Users inner join Roles on Roles.role_id = Users.role_id where Users.username = %s and Roles.name != %s"
                rows = self.database_connector.execute_query(query, (username,login_mng.role))
                print(f"Uzivatel : {username}:\n")
                print("{:<5} {:<20} {:<20} {:<5}".format("ID", "Uzivatelske jmeno","heslo","Role"))
                print("-" * 60)
                for row in rows:
                    print("{:<5} {:<20} {:<20} {:<5}".format(row[0], row[1] ,row[2], row[3]))
                print("\n")