print(10 > 3)
print(10 >= 3)
print(10 < 3)
print(10 <= 3)


# Zuweisen
x = 10 

# Vergleich
print(x == 10) # ob x gleich 10 ist --> True
print(x != 10) # ob x nicht gleich 10 ist --> False
print()

################################
# several conditions : and or 
x = 10 
y = 20 

print(x == 10  and y == 20 )
print(x == 10  or y == 500 )


print(x != 30  or y != 30 )
print(x != 30  and y != 30 )
print()

######################################
# not  --> wechselt von True <-> False
anwesend = True 

print(not anwesend)

######################################
# in 
course = "Einführung in Python"

print("Py" in course) # True
print("py" in course) # False