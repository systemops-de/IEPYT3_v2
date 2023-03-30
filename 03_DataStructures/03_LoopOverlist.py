teilnehmende_list = ["Thomas", "Ingo", "Sara", "Lena", "Julia", "Frank", "Mattias", "Sabine"]

for teilnehmende in teilnehmende_list:
    print(teilnehmende)
print()



################################################

teilnehmende_list = ["Thomas", "Ingo", "Sara"]

for tn in enumerate(teilnehmende_list):   # tn: Tuple (index, value)
    print(tn) # (1, 'Ingo')
print()


for tn in enumerate(teilnehmende_list):   # tn: Tuple (index, value)
    print("Index:", tn[0], "Value:", tn[1]) # (1, 'Ingo')


# enumerate with unpacking 
for index, value in enumerate(teilnehmende_list):
    print(index, value) 


########################################################
# Explanation of enumerate--->

teilnehmende_list = ["Thomas", "Ingo", "Sara"]

# enumerate() --
for idx, val in [ (0 , "Thomas") , (1,"Ingo" ), (2 ,"Sara") ]:
    print(idx, val)

print()
############################
# Change the start value of the index instead of 0 --> some number

teilnehmende_list = ["Thomas", "Ingo", "Sara"]

for index, value in enumerate(teilnehmende_list, 100):
    print(f"{index}. {value}")


########################################################
user = [ "Thomas", ("VW", "Car"), True, 45 , ["A", "B"] ]

for index, value in enumerate(user):
    print(index, value)