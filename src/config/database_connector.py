import configparser
import mysql.connector


class DatabaseConnector:
    _instance = None
    
    def __new__(cls,path_to_config_file):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.config_file_path = path_to_config_file
            cls._instance.load_config()
            cls._instance.connect()
        return cls._instance

    def load_config(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)
 
        


    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.config.get('Database', 'host'),
            user=self.config.get('Database', 'user'),
            password=self.config.get('Database', 'password'),
            database=self.config.get('Database', 'database')
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        if params is None:
            self.cursor.execute(query)
        else:
            self.cursor.execute(query, params)
        return self.cursor.fetchall()


    def close_connection(self):
        self.cursor.close()
        self.connection.close()

