###################################################
# E1: Sum of all values  --> output: 600
###################################################
# mydict = {
#     "val1": 100,
#     "val2": 200,
#     "val3": 300,
# }

# total = 0
# for val in mydict.values():
#     total += val 

# print("Sum:", total)



###################################################
# E2: Remove the key which is defined by user
###################################################
# user_input= input("Which Key: ").strip()

# user = {"id": 100, 
#         "first_name": "Thomas", 
#         "age": 55, 
#         "anwesend": True}
# print(user) # show orignal


# # Check if the key exists
# if user_input in user:
#     user.pop(user_input, "Not found")
# else:
#     print("The key does not exist")

# print(user) # show after changes

###################################################
# E3: Multiply of all values  --> output: 6
###################################################
# mydict = {
#     "val1": 1,
#     "val2": 2,
#     "val3": 3,
# }
 
###################################################
# E4:   NATO Alphabet: The user enters his username, and the python program retrieves the NATO alphabet for the username. 
# It a charachter not found, show the user 'Not found'
###################################################
""" 
A: Alpha
B: Bravo
C: Charlie
D: Delta
E: Echo
F: Foxtrott
...
"""

##### The simulation
""" 
user name: ABDEG

NATO Alphabet:
A: Alpha
B: Bravo
D: Delta
E: Echo
G: Not found
"""

nato_alphabet = {
    "A" : "Alpha",	"N" : "November",
    "B" : "Bravo",	"O" : "Oscar",
    "C" : "Charlie","P" : "Papa",
    "D" : "Delta",	"Q" : "Quebec",
    "E" : "Echo",	"R" : "Romeo",
    "F" : "Foxtrot","S" : "Sierra",
    "G" : "Golf",	"T" : "Tango",
    "H" : "Hotel",	"U" : "Uniform",
    "I" : "India",	"V" : "Victor",
    "J" : "Juliett","W" : "Whiskey",
    "K" : "Kilo",	"X" : "X-Ray",
    "L" : "Lima",	"Y" : "Yankee",
    "M" : "Mike",	"Z" : "Zulu"
}


user_name = input("Enter user name: ").upper()  # "VIKTOR"


for char in user_name: #  "VIKTOR"
    
    #### 1. Variante
    # Check if a key in nato alphabet       
    # if char in nato_alphabet:
    #     print(char , ":", nato_alphabet.get(char, "Not found"))

    #### 2. Variante
    print(char , ":", nato_alphabet.get(char, "Not found"))  # or with f string



 