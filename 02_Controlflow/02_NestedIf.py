# Nested If --> If Block in anderen If Block

temperature = 35 
humadity = 30

if temperature >= 30:
    if humadity >= 50:
        print("Klima aus")
    else:
        print("Klima an")


print()
############################
# Online Shop
age = 17 #   alter >= 18
payment_method  = False  


if age >= 18:
    if payment_method == True:
        print("Zur Kasse bitte")
    else:
        print("Du muss BZ-Methode eingeben!") 
else:
    print("Du bist zu jung")

