from simple_colors import *


class Printer:
    def print_admin_section(self):
        print(red('Admin sekce', 'bold'))
    def print_bold_white(self,name):
        print(black(f"{name}",'bold'))