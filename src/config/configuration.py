import configparser
import mysql.connector


class DatabaseConnector:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.config_file_path = 'config.ini'
            cls._instance.load_config()
            cls._instance.connect()
        return cls._instance

    def load_config(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)
        self.db_config = self.config['Database']

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.db_config['Host'],
            user=self.db_config['User'],
            password=self.db_config['Password'],
            database=self.db_config['Database']
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
