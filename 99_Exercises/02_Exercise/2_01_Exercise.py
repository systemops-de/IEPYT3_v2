""" 
Welcome to TELEKOM
~~~~~~~~~~~~~~~~~~

Language/Sprache
~~~~~~~~~~~~~~~~
[1] EN
[2] DE
[3] SP

Your choice> 1

What is your first name? thomas
What is your last name ? meier

Welcome Customer, Thomas MEIER!
"""

# Header
print(" Welcome to TELEKOM ")
print("~" * 20)

# Languuage
print("Language/Sprache")
print("~" * 20)

# print("[1] EN","\n[2] DE","\n[3] SP")
# print("[1] EN")
# print("[2] DE")
# print("[3] SP")
1
menu = """
[1] EN
[2] DE
[3] SP
"""
print(menu)


# User Choice of the language
user_lang = int(input("Your choice: "))

if user_lang == 1: # EN
    first_name = input("What is your first name?").title()    
    last_name = input("What is your last name?").upper()
    
    print(f"\nWelcome Customer: {first_name} {last_name}")
    
elif user_lang== 2: # DE
    first_name = input("Wie ist Ihr Vorname?: " ).title()    
    last_name = input("Wie ist Ihr Nachname?: " ).upper()
    
    print(f"\nHerzlich Willkommen Kunde: {first_name} {last_name}")

elif user_lang== 3: # SP
    first_name= input("Cuál es tu primer nombre?: ").title()    
    last_name = input("Cuál es tu apellido?: ").upper()    
    print(f"\nBienvenido cliente: {first_name} {last_name}")

else:
    print("Please choose 1,2 or 3!")