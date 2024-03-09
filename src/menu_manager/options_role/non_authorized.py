
options = {}

class Non_authorized_role:
    def __init__(self):
        pass
    def select_option_non_authorized(self,login_mng):
        choice = str(input())
        match choice:
            case "1":
                login_mng.login()
            case "2":
                 exit()
            case _:
                print("\nTato volba není dostupná\n")
    def print_options_non_authorized(self,path_to_guest_option_json):
        with open(path_to_guest_option_json) as json_file:
            options_from_json = json.load(json_file)
            options.update(options_from_json)
            for key, value in options_from_json.items():
                print(f"{key}) {value}") 