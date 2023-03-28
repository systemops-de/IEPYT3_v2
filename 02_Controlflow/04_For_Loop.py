for teinehmende in ["Thomas", "Ingo", "Sara", "Lena", "Mattias", "Julia", "Sabine"]:
    print("Hallo", teinehmende)
    print("Welches BKG ?")
    print("Python Vorkenntnisse? ")
    print()


for num in [1,2,3,4,5]:
    print(num)


for num in [10,20,30,40,50]:
    print("Number: " , num)



for char in "Python Course":
    print(char)
print() 


for num in [1,2,3,4,5]:
    print(num, end = " ")
print()


# range --> generates numbers
"""
range(startval, endvalue, step)
range(10):  0 --> 9
range(5, 10) : 5 -->  9
range(1, 20, 2): 1, 3 ,5 ,7 ,....., 19
"""

for num in range(5, 11,2):
    print(num)
print()

for num in range(5 , -5 , -1):
    print(num)


for num in range(11):
    print(num, "*" * num)

print()

##############################################

counter = 1

for tn in ["Thomas", "Ingo" , "Sara", "Lena"]:   
    print(f"{counter}. {tn}")    
    counter  += 1 # Inkemrent den Zähler um 1



""" 
1. Thomas
2. Ingo
3. Sara
4. Lena
"""
print()
#############################################

for num in [1,2,3,4,5]:
    if num == 3:
        print("Banana")
    else:
        print(num)
print() 

for num in range(1,21):
    if num % 2 == 0: # es gibt kein Rest --> Even Gerade
        print(num)


print()
#########################################
# Nested For