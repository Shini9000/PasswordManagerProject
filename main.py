import string
import random
import time

print("Welcome to the PasswordManager Application!"
      "\nFor more information please go to the github @"
      "\nhttps://github.com/Shini9000/PasswordManagerApplication"
      "\nAnd thank you for downloading and testing my application :)")
'''
True loop
'''
while True:
    '''
    Main menu loops
    '''
    user_input = input("Choose an option: "
                       "\n\n1. Generate Password "
                       "\n2. View Passwords "
                       "\n3. View Accounts "
                       "\n4. Add Account "
                       "\n5. Delete Account "
                       "\n6. Exit Application "
                       "\n\nEnter Input: ")
    try:
        val = int(user_input)
    except ValueError:
        print("not a digit")
    # Exit code
    if val == 6:
        print("GoodBye")
        exit()
    # Delete account code
    elif val == 5:
        print("Please select an account to delete: "
              "\nList accounts ~")
        delete_account = input("Choose an account to delete: ")
        print("no accounts")
        break
    # Add account code
    elif val == 4:
        print("Add an Account: ")
        break
    # Load account txt file (Loading not implemented as of V-Pre1.0.0
    elif val == 3:
        print("Loading Accounts database...")
        time.sleep(3)
        fl = open("database.txt", "r")
        print(fl.read())
        break
    # Load password txt file (Loading not implemented as of V-Pre1.0.0
    elif val == 2:
        print("Loading Passwords database...")
        time.sleep(3)
        fl = open("passwordhistory.txt", "r")
        print(fl.read())
        user_option = input("Would you like to 'Clear' or 'Exit'? ")
        # Clear the password file from inside the programme
        if user_option.lower() == "clear":
            with open("passwordhistory.txt", "r+") as fl:
                fl.truncate()
                fl.seek(0)
        else:
            print("Going back.")
    # Generate a new password
    elif val == 1:
        print("Generate a new password")
        password_type_select = input("Select an type: "
                                     "\n1. Uppercase "  # ABC
                                     "\n2. Lowercase "  # abc
                                     "\n3. Numbers "  # 123
                                     "\n4. Mix "  # Ab3
                                     "\n5. GenericPassword (Cap,Num and Sym"  # Ab3!
                                     "\n6. Debug(Unsafe size) "  # Size of 200000
                                     "\n\nEnter selection: ")
        try:
            selection = int(password_type_select)
        except ValueError:
            print("not a digit")

        if selection == 1:
            print("selected 1")
            letters = string.ascii_uppercase
            result_string = ''.join((random.choice(letters) for i in range(int(input("Select a password length: ")))))
            result_string.startswith("\n")
            print("\n" + result_string + "\n")

        elif selection == 2:
            print("selected 2")
            letters = string.ascii_lowercase
            result_string = ''.join((random.choice(letters) for i in range(int(input("Select a password length: ")))))
            result_string.startswith("\n")
            print("\n" + result_string + "\n")

        elif selection == 3:
            print("selected 3")
            numbers = string.digits
            result_string = ''.join((random.choice(numbers) for i in range(int(input("Select a password length: ")))))
            result_string.startswith("\n")
            print("\n" + result_string + "\n")

        elif selection == 4:
            print("selected 4")
            generic_letters = string.ascii_letters
            result_string = ''.join(
                (random.choice(generic_letters) for i in range(int(input("Select a password length: ")))))
            result_string.startswith("\n")
            print("\n" + result_string + "\n")

        elif selection == 5:
            print("selected 5")
            string_letters = string.ascii_letters
            string_numbers = string.digits
            string_symbols = string.punctuation
            string_line = string_letters + string_symbols + string_numbers
            result_string = ''.join(
                (random.choice(string_line) for i in range(int(input("Select a password length: ")))))
            result_string.startswith("\n")
            print("\n" + result_string + "\n")

            # Check if password meets requirements
        if input("Does this password fulfill the requirements?"
                 "\nY - Continue"
                 "\nN - ReGenerate"
                 "\n\nSelect: ").__contains__("n"):
            print("Regenerating your password")
            time.sleep(2)
            print("This feature is not ready as of V-Pre1.0.0")

        if input("Would you like to save this Password? "
                 "\n Y "
                 "\n N "
                 "\n\nSelect: ").__contains__("y"):
            print("Saving.")
            time.sleep(2)
            with open("passwordhistory.txt", "a") as fl:
                spacer = "\n"
                fl.writelines(spacer + result_string)
                fl.close()
            print("Saved.")
        else:
            print("Didn't save password.")
