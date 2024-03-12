from simple_colors import *


class Printer:
    def print_admin_section(self):
        print(red('Admin sekce', 'bold'))
    def print_bold_white(self,name):
        #print(black(f"{name}",'bold'))
        return black(f"{name}",'bold')
    def print_role(self,role):
        if role == "Admin": 
            return red(f"{role}",'bold')
        elif role =="Manager":
            return green(f"{role}",'bold')
        elif role == "Employee":
            return yellow(f"{role}",'bold')
        elif role == "Guest":
            return black(f"{role}",'bold')