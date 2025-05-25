import string
import random
import sys

allowed_special_characters = ["@","#","$","%","&","?","!"]
def instructions():
    print('''Welcome to Ndigitals Password generator.
This program generates secure passwords based on requirements that you provide. They include:
Length of characters, special characters, uppercase letters, and numbers.
Type 'close' to end this program.
''')

def readUserCriteria():
    length = ""
    while length != "close":
        print("Type how long you want the password to be\n")
        length = input("Length of password: ")
        if length == "close":
            closeProgram()
        length = validateLength(length)
        # if length == "too small":
        #     print("Password must be at least 6 characters")
        if length == "error":
            print("Length entered is not allowed. Password must be at least 6 characters. A max length of 60 characters is allowed")
        else:
            break
    special_characters = ""
    while special_characters != "close":    
        print("Type the special characters that you would like as part of the password. Seperate each one with a comma\nAt least one special character must be used for a strong password.\nType 'all' if you want the generator to select special characters for you. NB: The only allowed characters are '@,#,$,%,&,?,!'.\n")
        special_characters = input("Special Characters: ")
        if special_characters == "close":
            closeProgram()
        special_characters = validateSpecialCharacters(special_characters)
        if special_characters == "all":
            special_characters = allowed_special_characters
            break
        elif special_characters != "error":
            break
        else:
            print("One of the characters you entered isn't allowed\n")
    uppercase = ""
    while uppercase != "close":  
        print("Do you want UPPERCASE letters as compulsory in the password? Type Yes or No\n")
        uppercase = input("Uppercase: ")
        if uppercase == "close":
            closeProgram()
        uppercase = validateYesOrNo(uppercase)
        if uppercase != "error":
            break
        else:
            print("Only 'yes' or 'no' are accepted as answers\n")
    numbers = ""
    while numbers != "close":
        print("Do you want numbers compulsory in the password? Type Yes or No\n")
        numbers = input("Numbers: ")
        if numbers == "close":
            closeProgram()
        numbers = validateYesOrNo(numbers)
        if numbers != "error":
            break
        else:
            print("Only 'yes' or 'no' are accepted as answers\n")
    
    return {"length":length, "uppercase":uppercase, "numbers":numbers, "special_characters":special_characters}


def validateLength(length):
    if length == "0":
        return "error"
    try:
        length = int(length)
    except(ValueError):
        return "error"
    if length <= 5:
        return "error"
    elif length> 50:
        return "error"
    return length

def validateSpecialCharacters(special_characters):
    if special_characters.lower() == "all":
        return "all"
    special_characters = special_characters.split(",")
    for character in special_characters:
        if character not in allowed_special_characters:
            return "error"
    return special_characters

def validateYesOrNo(response):
    if response.lower() == "yes":
        return "yes"
    elif response.lower() == "no":
        return "no"
    else:
        return "error"

def passwordGenerator(length, uppercase="yes", numbers="yes",special_characters=["@","#","$","%","&","?","!"]):
    password = ""
    
    if uppercase == "yes" and numbers == "yes":
        shuffling_list = ["special_characters", "uppercase", "numbers", "lowercase"]
        password_character = random.choice(string.ascii_uppercase)
        password += password_character
        password_character = random.choice(string.digits)
        password += password_character
        password_character = random.choice(special_characters)
        password += password_character
        
    elif uppercase == "no" and numbers == "yes":
        shuffling_list = ["special_characters", "numbers", "lowercase"]
        password_character = random.choice(string.digits)
        password += password_character
        password_character = random.choice(special_characters)
        password += password_character
        password_character = random.choice(string.ascii_lowercase)
        password += password_character
    elif uppercase == "yes" and numbers == "no":
        shuffling_list = ["special_characters", "uppercase", "lowercase"]
        password_character = random.choice(string.ascii_uppercase)
        password += password_character
        password_character = random.choice(special_characters)
        password += password_character
        password_character = random.choice(string.ascii_lowercase)
        password += password_character
    
    elif uppercase == "no" and numbers == "no":
        shuffling_list = ["special_characters","lowercase"]
        password_character = random.choice(special_characters)
        password += password_character
        password_character = random.choice(string.ascii_lowercase)
        password += password_character
        password_character = random.choice(string.ascii_lowercase)
        password += password_character
    for i in range(length-3):
        password_character_type = random.choice(shuffling_list)
        if password_character_type == "special_characters":
            password_character = random.choice(special_characters)
        elif password_character_type == "uppercase":
            password_character = random.choice(string.ascii_uppercase)
        elif password_character_type == "numbers":
            password_character = random.choice(string.digits)
        elif password_character_type == "lowercase":
            password_character = random.choice(string.ascii_lowercase)
        password += password_character
    
    return password

def runProgram():
    run_again = True
    while run_again == True:
        instructions()
        password_criteria = readUserCriteria()
        check_for_special_characters = password_criteria.get("special_characters", "none")
        if check_for_special_characters == "none":
            password = passwordGenerator(password_criteria["length"], password_criteria["uppercase"], password_criteria["numbers"])
        else:
            password = passwordGenerator(password_criteria["length"], password_criteria["uppercase"], password_criteria["numbers"],password_criteria["special_characters"])

        print("\n")
        print(f"Your generated password is {password}")
        print("\n")

def closeProgram():
    print("Thanks for creating strong passwords with us, Cheers")
    sys.exit()

runProgram()