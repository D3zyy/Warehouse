import json 

options_supplier = {}
class supplier_manager:
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
    def print_supplier_options(self,path_to_supplier_options):
        with open(path_to_supplier_options) as json_file:
            options_from_json = json.load(json_file)
            options_supplier.update(options_from_json)
            for key, value in options_from_json.items():
                print(f"{key}) {value}")