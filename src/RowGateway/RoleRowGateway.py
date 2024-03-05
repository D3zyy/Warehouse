from src.RowGateway.RowGateway_polymorphism.RowGateway  import RowGateway 

class RoleRowGateway(RowGateway):

    def findById(self, id):
        query = f"SELECT * FROM Roles WHERE id = %s"
        cursor = self.database_connector.cursor()
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        cursor.close()
        return row
    def findByUsername(self, username):
        query = f"SELECT * FROM Roles WHERE name = %s"
        cursor = self.database_connector.cursor()
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        cursor.close()
        return row
    def generate_report(self):
        query = "SELECT * FROM Roles"
        rows = self.database_connector.execute_query(query)
        self.database_connector.close_connection()
        print("Role Report:")
        print("{:<5} {:<20}".format("ID", "Name"))
        print("-" * 60)
        for row in rows:
            print("{:<5} {:<20}".format(row[0], row[1]))


