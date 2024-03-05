from src.config.database_connector import DatabaseConnector 
from src.RowGateway.RoleRowGateway import RoleRowGateway 
from src.menu_options.menu_options import welcome_message

dc = DatabaseConnector('config/config.ini')

r = RoleRowGateway(dc)
r.generate_report()

    #from src.RowGateway.RoleRowGateway import r
    #r.generate_report()

