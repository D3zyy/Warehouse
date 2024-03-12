from simple_colors import *


class Printer:
    def print_admin_section(self):
        print(red('Admin sekce'))
    def print_bold_white(self,name):
        return black(f"{name}")
    def print_role(self,role):
        if role == "Admin": 
            return red(f"{role}")
        elif role =="Manager":
            return green(f"{role}")
        elif role == "Employee":
            return yellow(f"{role}")
        elif role == "Guest":
            return black(f"{role}")