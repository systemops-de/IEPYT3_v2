temperature = 35 

if temperature >= 30:
    print("Klima an")
else:
    print("Klima aus")

print()
############################################
# Hard limits are explizitly defined --> no problem with the order

temperature = 20 

if temperature >= 30:
    print("Es ist heiß")

elif temperature < 30   and temperature >= 20:
    print("Es ist warm")

elif temperature < 20 and temperature >= 10:
    print("Es ist cool")

elif temperature < 10 and temperature >= 0:
    print("Es ist kalt")
else:
    print("Negative range")

print()

############################################
# The order is correct --> everything is correct

temperature = -5

if temperature >= 30:
    print("Es ist heiß")

elif temperature >= 20:
    print("Es ist warm")

elif temperature >= 10:
    print("Es ist cool")

elif temperature >= 0:
    print("Es ist kalt")
else:
    print("Negative range")
print()

############################################
# The order of the conditions is wrong --> 25 Grad wird als Kalt vom System definiert
# The order of the conditions is very important
temperature = 25

if temperature >= 30:
    print("Es ist heiß")

elif temperature >= 0:
    print("Es ist kalt")

elif temperature >= 20:
    print("Es ist warm")

elif temperature >= 10:
    print("Es ist cool")


else:
    print("Negative range")

print()

############################################
# Hard limits are explizitly defined --> no problem with the order

temperature = 5 


if temperature >= 30:
    print("Es ist heiß")

elif  20 <= temperature < 30:
    print("Es ist warm")

elif 10 <= temperature < 20:
    print("Es ist cool")

elif 0 <= temperature < 10:
    print("Es ist kalt") 
else:
    print("Negative range")

print()




