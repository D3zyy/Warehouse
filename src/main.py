from src.config.database_connector import DatabaseConnector 
from src.RowGateway.RoleRowGateway import RoleRowGateway 
from src.menu_manager.menu_options import *

dc = DatabaseConnector('config/config.ini')
option_manager = Options_manager()

while True:
    option_manager.welcome_message()
    option_manager.print_options('menu_manager/options.json')
    option_manager.select_option()






#r = RoleRowGateway(dc)
#r.generate_report()



