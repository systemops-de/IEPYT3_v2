# Im Terminal: Ctrl (Strg) + c ---> cancel
temperature = 35 


while temperature > 30:
    
    print("Klima an: ", temperature)
    temperature -= 1


print()
################################################

user_input = ""

while user_input != "exit":
    user_input = input("Enter a word: ")
    print("Echo", user_input)
 