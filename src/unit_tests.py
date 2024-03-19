from security.login import Login_manager
from config.database_connector import DatabaseConnector
from config.Initialization import Settings
import configparser
import unittest

class Tester(unittest.TestCase):

    def test_isLoggedIn_by_default(self):
        login_mng = Login_manager()

        self.assertEqual(login_mng.isLoggedIn(),False)
    def test_singleton_instance(self):

        config_path = 'config/config.ini'
        connector1 = DatabaseConnector(config_path)
        connector2 = DatabaseConnector(config_path)
        self.assertIs(connector1, connector2)
    def test_loading_path_to_config(self):
        config_path = 'config/config.ini'
        s = Settings(config_path)
        self.assertEquals(s.config_file_path,config_path)
    def test_loading_default_user_password(self):
        config_path = 'config/config.ini'
        config = configparser.ConfigParser()
        config.read(config_path)
        s = Settings(config_path)
        self.assertEquals(s.default_user_password,config.get('DefaultUser', 'password'))
    def test_loading_default_user_username(self):
        config_path = 'config/config.ini'
        config = configparser.ConfigParser()
        config.read(config_path)
        s = Settings(config_path)
        self.assertEquals(s.default_user_username,config.get('DefaultUser', 'username'))
    def test_loading_default_user_role(self):
        config_path = 'config/config.ini'
        config = configparser.ConfigParser()
        config.read(config_path)
        s = Settings(config_path)
        self.assertEquals(s.default_user_role,config.get('DefaultUser', 'role'))
    def test_loading_warehouse_name(self):
        config_path = 'config/config.ini'
        config = configparser.ConfigParser()
        config.read(config_path)
        s = Settings(config_path)
        self.assertEquals(s.warehouse_name,config.get('Warehouse', 'name'))

if __name__ == '__main__':
    unittest.main()
