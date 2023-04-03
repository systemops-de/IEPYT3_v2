"""
Set:
~~~~
1. No Duplication
2. No Indexing (Un-indexed) --> which does not offer myset[0]
3. Unordered : each time you may get a new order ot items
4. unchangable: you can add and remove , but not to update an item
"""


# Define a set
myset = {1, 2, 5, 10}
print(myset, type(myset))

# conversion function set()
myset = set([1, 2, 2, 3, 3, 3])
print(myset, type(myset))


# Add new items in set
myset.add(8)
print(myset, type(myset))


# len of set
print(len(myset))


#################################
# Operations between sets
myset1 = {1, 2, 5, 10}
myset2 = {2, 5, 10, 20, 30}

# Common between sets
print(myset1 & myset2)  # and : {2, 10, 5}

# Combine two sets
print(myset1 | myset2)  # or :{1, 2, 5, 10, 20, 30}

# everything without the common values
print(myset1 ^ myset2)  # xor : {1, 20, 30}


# only the items in the first set without the common values  a - b
print(myset1 - myset2)  # a-b : {1}


#################################
# Using Methods
#################################
# 1. union (OR)

tn_set1 = {"Thomas", "Ingo"}
tn_set2 = {"Lena", "Lena", "Julia", "Thomas"}
total = tn_set1.union(tn_set2)
print(total)  # {'Thomas', 'Julia', 'Lena', 'Ingo'}


# 2. intersect (and) :common values
total = tn_set1.intersection(tn_set2)
print(total)  # {'Thomas'}


# difference
total = tn_set1.symmetric_difference(tn_set2)
print(total)  # {'Lena', 'Ingo', 'Julia'}


########################
# Check if a value in a set
tn_set1 = {"Thomas", "Ingo"}
print("Thomas" in tn_set1)  # True
print("Thomass" in tn_set1)  # False

print()
########################
# Iterate over a set
# tn_set = {"Lena", "Lena", "Julia", "Thomas", ["A", "B"]}
tn_set = {"Lena", "Lena", "Julia", "Thomas"}

mylist = ["A", "B"]
mytuple = ("AA", "BB")
mydict = {"car": "VW", "KZ": "AA12345"}
myset2 = {"HH", "MM", "NN"}

# Add the items to the set
tn_set.update(mylist)
tn_set.update(mytuple)
tn_set.update(mytuple)
tn_set.update(mydict)  # Only the keys will be added
tn_set.update(myset2)


print(tn_set)
for tn in tn_set:
    print(tn)


###############################
# Remove items

print(tn_set)

tn_set.remove("Lena")
print(tn_set)

# ERROR if the value does not exist
# tn_set.remove("Banana")  # -> ERROR if the value does not exist
# print(tn_set)


# Alternative using discard
tn_set.discard("Banana")  # -> nothing happend if the value does not exists
print(tn_set)


# pop : will remove a random item
tn_set.pop()  # -> will remove a random item
print(tn_set)

deleted_item = tn_set.pop()
print(deleted_item)  # car


# clear all items -> the variables is still in memory
tn_set.clear()
print(tn_set)

tn_set.add("Thomas")

# ERROR : unchangable items
# tn_set[0] = "AAA"


# alternative
del tn_set  # delete the variable from the memory
##################
# Example:
user_list = []

while True:
    user_input = input("Enter a word: ")

    if user_input == "0":
        break

    user_list.append(user_input)


# Get only unique entries
user_wishes = list(set(user_list))
user_wishes.sort()
print(user_wishes)
