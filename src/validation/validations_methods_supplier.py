import re

def validate_postal_code():
    while True:
        postal_code = input("Zadejte postovni smerovaci cislo (PSC): ")
        if not re.match(r'^\d{3} \d{2}$', postal_code):
            print("Neplatný formát PSC. Zadejte 3 cislice, mezera a pak 2 cislice.")
        else:
            return postal_code

def validate_city():
    while True:
        city_name = input("Zadejte nazev mesta: ")
        if not re.match(r'^[a-zA-Z ]{3,}$', city_name):
            print("Neplatny format názvu mesta. Zadejte pouze pismena a mezery, alespon 3 znaky.")
        else:
            return city_name


def validate_street():
    while True:
        street_name = input("Zadejte název ulice: ")
        if len(street_name) < 3:
            print("Název ulice musí obsahovat alespoň 3 znaky.")
        elif not re.match(r'^[a-zA-Z0-9 ]{3,}$', street_name):
            print("Neplatny format nazvu ulice. Zadejte pouze pismena, cislice a mezery.")
        else:
            return street_name


def validate_phone_number():
    pattern = r'^\+\d{3} \d{3} \d{3} \d{3}$'
    
    while True:
        phone_number = input("Zadejte telefoni cislo dodavatele ve formatu [+XYZ XXX XXX XXX] : ")
        if re.match(pattern, phone_number):
            return phone_number
            
        else:
            print("Neplatny format telefonniho cisla. Zkuste to znovu.")


def check_existance_of_id(id,table,connector):
       query = f"SELECT address_id FROM {table} WHERE address_id = %s "
       result = connector.execute_query(query, (id,))
       if result:
             return True
       else: 
             return False

def validate_number(name):
        while True:
           try:
               id = int(input(f"Zadejte id {name} : "))
               if id > 0:
                     return id
               else:
                         print("Id musi byt kladne cele cislo, zkuste znovu.")
           except ValueError:
                        print("Id musi byt cele cislo, zkuste znovu.")

def validate_name(name):
    while True:
        username = input(f"Zadejte jmeno {name}: ")
        if username.isdigit():
            print("Jmeno nemuze byt cislo, zkuste znovu.")
        elif not (re.match(r'^[a-zA-Z .]{3,}$', username) and len(username) >= 3):
            print("Jmeno muze obsahovat pouze pismena, tečky a mezery a musi mit minimalne 3 znaky. Zkuste to znovu.")
        else:
            return username
def new_address():
     while True:
            vyber = str(input(" Pridani adresy dodavatele \n 1)  Chcete zadat id jiz existujici adresy \n 2)  vytvorit novou adresu"))
            match vyber:
                case "1":
                        return False
                case "2":
                        return True
                case _:
                        print("Tato možnost neni dostupna")
