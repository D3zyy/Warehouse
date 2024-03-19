from src.TableGateway.TableGateway_polymorphism.TableGateway  import TableGateway 



class RoleTableGateway(TableGateway):
    def __init__(self,database_connector):
        super().__init__(database_connector)
    def get_all_roles(self):
        print("\n")
        query = "SELECT role_id,name from Roles"
        rows = self.database_connector.execute_query(query)
        print("Role v  systemu:")
        print("{:<5} {:<5} ".format("ID","Jmeno role"))
        print("-" * 20)
        for row in rows:
            print("{:<5} {:<5}".format(row[0],row[1]))
        print("\n")
   