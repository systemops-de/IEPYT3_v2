import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


# Write all numbers between 10 and 20 

with open("file2.txt", mode = "a", encoding= "UTF-8") as file:
    for num in range(10, 21):
        
        file.write(f"{num}\n")


########################################################################
# Write user inputs to a file --> 1. Variante
wishes = ""

while True:
    user_input = input("Enter your wish> ")

    if user_input == "0":
        break 

    wishes = f"{wishes}\n{user_input}"



with open("file3.txt", mode = "a", encoding= "UTF-8") as file:
    file.write(wishes)