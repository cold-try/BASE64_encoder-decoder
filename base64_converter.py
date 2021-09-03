from ascii_dictionnary import ascii_table 
from base64_dictionnary import base64_table


def find_key_with_value(val, dico): 
    for key, value in dico.items(): 
        if value == val: 
            return key 
    return "Cette valeur n'existe pas"


def to_base_64():
    
    total_binary = ""
    result_base64 = ""
    initialisation = 0
    multiple = 6
    choice = input("Pour encoder une chaine de caractères entrez C - Pour une représentation binaire entrez n'importe quelle touche : ")
    print("")
    
    if choice.lower() == "c":
        to_convert = input("Veuillez entrer la chaîne de caractères à encoder en BASE64 : ")
        to_convert = to_convert.replace(" ", "")

        for caracter in to_convert:
            if caracter == '“' or caracter == '”':
                caracter = '"'
            total_binary = total_binary + ascii_table[caracter]
    else:
        to_convert = input("Veuillez entrer la représentation de données binaires à encoder en BASE64 : ")
        total_binary = to_convert.replace(" ", "")

    while initialisation < len(total_binary)//6:
        result_base64 = result_base64 + base64_table[total_binary[multiple-6:multiple]]
        initialisation = initialisation + 1
        multiple = multiple + 6

    print("")
    print("Résultat en BASE64 : " + result_base64)
    print("")


def from_base_64():

    total_code = ""
    initialisation = 0
    multiple = 8
    result = ""
    choice = input("Pour décoder du BASE64 en code binaire entrez B - Pour du texte entrez n'importe quelle autre touche : ")
    print("")

    if choice.lower() == "b":
        to_convert = input("Veuillez entrer la chaîne en BASE64 à décoder en représentation binaire : ")
        for letter in to_convert:
            total_code = total_code + find_key_with_value(letter, base64_table)

        while initialisation < len(total_code)//8:
            result = result + " " + total_code[multiple-8:multiple]
            initialisation = initialisation + 1
            multiple = multiple + 8
        
    else:
        to_convert = input("Veuillez entrer la chaîne en BASE64 à décoder en caractère normaux : ")
        for letter in to_convert:
            total_code = total_code + find_key_with_value(letter, base64_table)

        while initialisation < len(total_code)//8:
            result = result + find_key_with_value(total_code[multiple-8:multiple], ascii_table)
            initialisation = initialisation + 1
            multiple = multiple + 8

    print("")
    print("Résultat : " + result)
    print("")


###########################################################################################################

    
while True:
    print("")
    choice = input("BASE64 converter : E pour encoder - D pour décoder : ")
    print("")
    if choice.lower() == 'e':
        to_base_64()
        break
    elif choice.lower() == 'd':
        from_base_64()
        break
    else:
        print("")
        print("Nous n'avons pas compris votre choix, veuillez réessayer... (CTRL+C pour quitter)")
