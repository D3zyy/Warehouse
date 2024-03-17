import re 

def validate_name():
    while True:
        username = input(f"Zadejte jmeno : ")
        if username.isdigit():
            print("Jmeno nemuze byt cislo, zkuste znovu.")
        elif not (re.match(r'^[a-zA-Z .]{3,}$', username) and len(username) >= 3):
            print("Uzivatelske jmeno muze obsahovat pouze pismena, tečky a mezery a musi mit minimalne 3 znaky. Zkuste to znovu.")
        else:
            return username
def validate_password():
    while True:
        password = input("Zadejte heslo: ")
        if len(password) < 4:
            print("Heslo musí mít minimálně 4 znaky. Zkuste to znovu.")
        elif not any(char.isdigit() for char in password):
            print("Heslo musí obsahovat alespoň jedno číslo. Zkuste to znovu.")
        else:
            return password


def check_existance_of_user(connector):
    while True:
        name = input("Zadejte jmeno uzivatele : ")
        if len(name) < 3:
            print("Jmeno musi obsahovat aspon 3 znaky Zkuste to znovu.")
        elif name.isdigit():
            print("Jmeno nemuze byt cislo. Zkuste to znovu.")
        else:
            query = "SELECT username FROM Users WHERE username = %s"
            result = connector.execute_query(query, (name,))
            if result:  
                return name
            else:
                print("Uzivatel nebyl nalezen. Zkuste to znovu.")


            
