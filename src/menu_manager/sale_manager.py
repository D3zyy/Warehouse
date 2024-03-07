import json 

options_sale = {}
class sale_manager:
    def __init__(self):
        pass
    def execute(self,value):
        match value:
            case "1":
                print("VYTVORENI")
            case "2":
                print("EDITACE")
            case "3":
                print("ODSTRANENI")
            case _:
                print("\nTato volba není dostupná \n")
    def print_sale_options(self,path_to_sale_options):
        with open(path_to_sale_options) as json_file:
            options_from_json = json.load(json_file)
            options_sale.update(options_from_json)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")