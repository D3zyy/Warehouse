import json
from src.config.Initialization import Settings



from src.menu_manager.options_role.guest_role import Guest_role
from src.menu_manager.options_role.employee_role import Employee_role
from src.menu_manager.options_role.manager_role import Manager_role
from src.menu_manager.options_role.admin_role import Admin_role
from src.menu_manager.options_role.non_authorized import Non_authorized_role

guest_role = Guest_role()
employee_role  = Employee_role()
manager_role  = Manager_role()
admin_role = Admin_role()     
non_authorized_role  = Non_authorized_role()     


#Cesta uvedena relativně kde je importován menu_options v main.py
settings1 = Settings('config/config.ini')

options = {}

class Options_manager:
    def __init__(self) -> None:
        pass
    def print_options_by_role(self,role_id):
        if role_id == 1:
            admin_role.print_options_admin('menu_manager/options_role_json/options_role_admin.json')
        elif role_id == 2:
             manager_role.print_options_manager('menu_manager/options_role_json/options_role_manager.json')
        elif role_id == 3:
             employee_role.print_options_employee('menu_manager/options_role_json/options_role_employee.json')
        elif role_id == 4:
               guest_role.print_options_guest('menu_manager/options_role_json/options_role_guest.json')
        else:
            non_authorized_role.print_options_non_authorized('menu_manager/options_role_json/options_role_non_authorized.json')
  
    

    
    def welcome_message(self):
        print(f"{settings1.warehouse_name} \n")

    def select_option(self,role_id,login_mng):
        if role_id == 1:
            admin_role.select_option_admin(login_mng,role_id)
        elif role_id == 2:
            manager_role.select_option_manager(login_mng,role_id)
        elif role_id == 3:
            employee_role.select_option_employee(login_mng,role_id)
        elif role_id == 4:
            guest_role.select_option_guest(login_mng,role_id)
        else:
            non_authorized_role.select_option_non_authorized(login_mng)
        #print(f"funguje : {options}")
                             
   



#welcome_message()
##print_options('options.json')
