import random

create_dict = {}
namepassword_dict = {}
edit_mode = 0
username_to_edit = ""

def start():
    global edit_mode
    createoredit = input("Welcome to the password generator! Would you like to make a new profile or edit an existing one? (Enter CREATE or EDIT):").lower().replace(" ","")
    while createoredit != "create" and createoredit != "edit" :
        createoredit = input("Please enter a valid input: Would you like to make a new profile or edit an existing one? (Enter CREATE or EDIT):").lower().replace(" ","")
    if createoredit == "create":
        edit_mode = 0
        create()
    elif createoredit == "edit":
        edit_mode = 1
        edit_prompt()


def create():
    global create_dict
    global edit_mode
    created_password = ""
    characters = input("How many characters would you like for your password to be?").lower().replace(" ","")
    while characters.isnumeric() == False:
        characters = input("Please enter a number! How many characters would you like for your password to be?").lower().replace(" ","")
    characters = int(characters)
    for i in range(1,characters+1):
        created_password += random.choice("abcdefghijklmnopqrstuvwxyz0123456789")
    while edit_mode == 0:
        username = input(f"Your password is {created_password}. What would you like for your username to be?").lower().replace(" ","")
        while username == "":
            username = input("Please enter a username. What would you like for your username to be?").lower().replace(" ","")
        create_dict[username] = ""
        create_dict[username] = created_password
        with open("savedpasswords.txt", "a") as f:
            for i in create_dict:
                f.write(f"{i}: {create_dict[i]} \n")
        startagain()
    while edit_mode == 1:
        return created_password
    

def edit_prompt():
    global namepassword_dict, username_to_edit
    print("You've entered the edit profile menu.")
    username_to_edit = input("What's the username of the profile you'd like to edit?")
    username_to_edit = find_username(username_to_edit)
    generateorenter = input("Would you like to generate a new password or edit a password? (Please enter either GENERATE or ENTER):").lower().replace(" ","")
    generateorenter = check_generate_or_enter(generateorenter)
    if generateorenter == "generate":
        generate_pass()
    elif generateorenter == "enter":
        enter_pass()

def find_username(checkforuser):
    with open("savedpasswords.txt", "r+") as f:
        c = f.read()
        c = c.split("\n")
        del c[-1]
        for pair in c:
            pair = pair.replace(" ","")
            pair = pair.split(":") 
            namepassword_dict[pair[0]] = pair[1]
    while checkforuser not in namepassword_dict:
        checkforuser = input("INVALID USERNAME: Which password would you like to retrieve? Please enter a valid username.")
        if checkforuser not in namepassword_dict:
            print("Here's a list of usernames for all the current profiles, please pick one:")
            for i in namepassword_dict:
                print(i)
    return checkforuser

def check_generate_or_enter(checkforvalidity):
    while checkforvalidity != "generate" and checkforvalidity != "enter":
        checkforvalidity = input("Please enter a valid option! Would you like to generate a new password, or enter your own password? (Please enter GENERATE or ENTER)").lower().replace(" ","")
    return checkforvalidity

def generate_pass():
    global username_to_edit
    namepassword_dict[username_to_edit] = create()
    print(f"Your new password for {username_to_edit} is {namepassword_dict[username_to_edit]}")
    with open("savedpasswords.txt", "w") as f:
        for i in namepassword_dict:
            f.write(f"{i}: {namepassword_dict[i]} \n")
    startagain()

def enter_pass():
    global username_to_edit
    new_pass = input("Please enter your new password:")
    while new_pass == "":
        new_pass = input("Invalid input. Please enter your new password:")
    namepassword_dict[username_to_edit] = new_pass
    with open("savedpasswords.txt", "w") as f:
        for i in namepassword_dict:
            f.write(f"{i}: {namepassword_dict[i]} \n")
    print(f"Your new password for {username_to_edit} is {new_pass}")
    startagain()

def startagain():
    againornotagain = input("Would you like to go back to the menu? (Y/N):").lower().replace(" ","")
    while againornotagain not in ("y", "n"):
        againornotagain = input(f"Please enter a valid option. Would you like to go back to the menu? (Y/N):").lower().replace(" ","")
    if againornotagain == "y":
        start()

start()