from src.config.Initialization import Settings

settings1 = Settings('../config/config.ini')
options = {
1 : "Prijemky..",
2 : "Vydejky..",
3 : "Objednavky",
4 : "",


}
def options():
    pass
def welcome_message():
    print(f"Welcome to {settings1.warehouse_name} \n")


    
welcome_message()