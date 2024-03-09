import re

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
                         print("Id musí být kladné celé číslo, zkuste znovu.")
           except ValueError:
                        print("Id musí být celé číslo, zkuste znovu.")

def validate_numberr(name):
      while True:
            username = input(f" Zadejte id {name} : ")
            if username.isdigit():
                print("Jmeno nemuze byt cislo, zkuste znovu.")
                
            elif not (re.match("^[a-zA-Z]*$", username) and len(username) >= 4):
                print("Jmeno muze obsahovat pouze pismena a musi mit minimalne 4 znaky. Zkuste to znovu.")
            else:
                 return username

def validate_name(name):
    while True:
        username = input(f"Zadejte jmeno {name}: ")
        if username.isdigit():
            print("Jmeno nemuze byt cislo, zkuste znovu.")
        elif not (re.match("^[a-zA-Z ]*$", username) and len(username) >= 3):
            print("Jmeno muze obsahovat pouze pismena a mezery a musi mit minimalne 3 znaky. Zkuste to znovu.")
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
