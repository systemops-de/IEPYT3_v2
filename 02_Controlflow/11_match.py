print("Enter your language")
print("[1] DE")
print("[2] EN")
print("[3] SP")


user_lang = input(">")

if user_lang == "DE":
    print("Hallo")
elif user_lang == "EN":
    print("Hello")
elif user_lang == "SP":
    print("Hola")


# ALternative
match user_lang:
    case "DE":
        print("Hallo")

    case "EN":
        print("Hello")        

    case "SP":
        print("Hola")
    
    case _:
        print("Nicht gefunden")
