import re

def validate_password():
    while True:
        password = input("Zadejte heslo: ")
        if len(password) < 3:
            print("Heslo musí mít minimálně 3 znaky.")
        elif not re.search(r'[a-zA-Z]', password):
            print("Heslo musí obsahovat alespoň jedno písmeno.")
        elif not re.search(r'\d', password):
            print("Heslo musí obsahovat alespoň jednu číslici.")
        else:
            return password

def validate_domain():
    while True:
        username = input(f"Zadejte nazev hosta : ")
        if username.isdigit():
            print("Jmeno nemuze byt cislo, zkuste znovu.")
        elif not (re.match(r'^[a-zA-Z .]{3,}$', username) and len(username) >= 3):
            print("Uzivatelske jmeno muze obsahovat pouze pismena, tečky a mezery a musi mit minimalne 3 znaky. Zkuste to znovu.")
        else:
            return username
def validate_username_db():
    while True:
        username = input("Zadejte jméno: ")
        if username.isdigit():
            print("Jméno nemůže být číslo, zkuste znovu.")
        elif not re.match(r'^[^"\'<>]+$', username):
            print("Uživatelské jméno může obsahovat pouze písmena, tečky a mezery . Zkuste to znovu.")
        else:
            return username
def validate_database_name():
    while True:
        username = input("Zadejte jméno databaze: ")
        if username.isdigit():
            print("Databaze nemůže být číslo, zkuste znovu.")
        elif not re.match(r'^[^"\'<>]+$', username):
            print("Databaze  může obsahovat pouze písmena, tečky a mezery . Zkuste to znovu.")
        else:
            return username
def validate_role():
    while True:
        role = input("Zadejte roly : ")
        match role.lower():
            case "admin":
                return "Admin"
            case "manager":
                return "Manager"
            case "employee":
                return "Employee"
            case "guest":
                return "Guest"
            case _:
                print("Tato role neni dostupna vybirejte pouze z (Admin,Manager,Employee,Guest)")