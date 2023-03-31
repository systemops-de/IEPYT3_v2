# While loop


#################################################################
# E1: Get different numbers from the user till 0 (exit point) --> 
#################################################################

""" 
Enter your number : 5
Enter your number : -1
Enter your number : 3
Enter your number : 4
Enter your number : -2
......
Enter your number : 0   -> exit point


All numbers are : 5 -1 3 4 -2 
All Even numbers are:  4 -2 
All Odd numbers are: 5 -1 3
"""

# all_numbers = []
# even_numbers = []
# odd_numbers = []

# while True:
#     user_input = int(input("Enter a number: "))

#     if user_input == 0:
#         break  # exit point
    
#     all_numbers.append(user_input)

#     if user_input % 2 == 0 : # Even Gerade
#         even_numbers.append(user_input)
#     else: # Odd - Ungerade
#         odd_numbers.append(user_input)

# print("All numbers:", all_numbers)
# print("Even numbers:", even_numbers)
# print("Odd numbers:", odd_numbers)


#################################################################
# E2: Restaurant
#################################################################

"""
Willkommen bei ACASA-Restaurant
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Menu
~~~~
Pizza Margeritta
Pizza Tunfisch
Salat Normal
Salat VIP


Wünschen:
~~~~~~~~
> Pizza Margeritta
> Pizza Tunfisch
> Salat VIP
> ...
> 0     -> exit point


Quittung(Auflistung):
~~~~~~~
Pizza Margeritta
Pizza Tunfisch
Salat VIP

Vielen Dank für Ihren Besuch.!

"""

# Greeting Meeting
print("Willkommen bei ACASA-Restaurant")
print("~" * 40)


# Show Menu 
print("Menu")
print("~~~~")
print("Pizza Margerritta")
print("Pizza Tunfisch")


menu = """
Menu
~~~~
Pizza Margeritta
Pizza Tunfisch
"""

print(menu)



# Get the user wishes
print("Wünschen:")
print("~" * 10)

user_wish_list = []

while True:
    user_input = input("> ").strip()

    if user_input == "0":
        break  # exit point

    # Validate if the user wish in the Menu
    if user_input not in menu:
        print("Leider nicht vorhaden")
        continue

    # Add the user wish to the collection_list
    user_wish_list.append(user_input)


# Receipt 
print("Quittung")
print("~" * 10)

for wish in user_wish_list:
    print(wish)



    