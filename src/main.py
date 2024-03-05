
from src.config.database_connector import DatabaseConnector 
from src.RowGateway.RoleRowGateway import RoleRowGateway 

dc = DatabaseConnector('config/config.ini')

r = RoleRowGateway(dc)
r.generate_report()
    #from src.RowGateway.RoleRowGateway import r
    #r.generate_report()

