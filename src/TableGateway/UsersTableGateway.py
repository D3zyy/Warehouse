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