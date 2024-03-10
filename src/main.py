from src.config.database_connector import DatabaseConnector 
from src.RowGateway.RoleRowGateway import RoleRowGateway 
from src.menu_manager.menu_options import *
from src.security.login import Login_manager

login_mng = Login_manager()
login_mng.load_config('config/config.ini')
dc = DatabaseConnector('config/config.ini')
option_manager = Options_manager()

try:
    while True:
        option_manager.welcome_message()
        login_mng.login_message()
        option_manager.print_options_by_role(login_mng.get_role())
        option_manager.select_option(login_mng.get_role(),login_mng)
except Exception as e:
    print(f"Nastala chyba : {e}")
except ValueError as e:
    print(e)
except KeyboardInterrupt as e:
    print(f"\nProgram ukončen klavesou")







#r = RoleRowGateway(dc)
#r.generate_report()



