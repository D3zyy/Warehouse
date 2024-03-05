import configparser

class Settings:
    def __init__(self,path_to_config_file):
        self.config_file_path =  path_to_config_file
        self.config = configparser.ConfigParser()
        self.config.read(self.config_file_path)
        self.default_user_username = self.config.get('DefaultUser', 'username')
        self.default_user_password = self.config.get('DefaultUser', 'password')
        self.default_user_role = self.config.get('DefaultUser', 'role') 
        self.warehouse_name = self.config.get('Warehouse', 'name')
