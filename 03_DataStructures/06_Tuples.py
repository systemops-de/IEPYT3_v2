""" 
Tupels use cases:
1. Read Only container
2. To protect the content of the tuple from direct change within the code
3. Some functions returns by default a TUPLE

"""


# Tuples are READ ONLY Container -> No adding, Editing , Removing

teilnehmende_tuple = ("Thomas", "Ingo", "Sara", "Lena", "Julia", "Frank", "Mattias", "Sabine")

print(teilnehmende_tuple, type(teilnehmende_tuple))

print(teilnehmende_tuple[0])
print(teilnehmende_tuple[1])
print(teilnehmende_tuple[-1])
print(teilnehmende_tuple[1:4])
print(teilnehmende_tuple[1:6:2])


for tn in teilnehmende_tuple:
    print(tn)

# You cannot edit a value
# teilnehmende_tuple[0] = "2232" ##-> error


##########################################################################
# I can re-define the value --> new memory address
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
teilnehmende_tuple = ("Thomas", "Ingo", "Sara", "Lena", "Julia", "Frank", "Mattias", "Sabine")
print(teilnehmende_tuple)

teilnehmende_tuple = ("Thomas", "Ingo", "Sara", "Lena", "Julia", "Frank", "Mattias", "Sabine", "Marc")
print(teilnehmende_tuple)


###########################################################################
# Work around to change the content of a tuple
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
teilnehmende_tuple = ("Thomas", "Ingo", "Sara")
print(teilnehmende_tuple)


# 1. Convert the tuple(read only) to an editable container (List)
tmp_list = list(teilnehmende_tuple)

# 2. add the changes to the temporary list
tmp_list.append("Marc")
tmp_list.append("Steffi")
tmp_list[0] = "Tomas"

# 3. Convert the temporary list back to a tuple and re-assign the variable tuple to the new created tuple
teilnehmende_tuple = tuple(tmp_list)
print(teilnehmende_tuple)


#########################################
# Single item within a tuple, neeeds a comman ',' at the end

x = ["A"]
print(x, type(x)) # ['A'] <class 'list'>

x = ("A")
print(x, type(x)) # A <class 'str'>


x = (50)
print(x, type(x)) # 50 <class 'int'>


x = (50,60)
print(x, type(x)) #  (50, 60) <class 'tuple'>

# One single item within the tuple .---> as a tuple
x = (60,)
print(x, type(x)) # (60,) <class 'tuple'>


################################################################
# Convert int to a tuple
x = 10
x = (10,)
print(x, type(x))

