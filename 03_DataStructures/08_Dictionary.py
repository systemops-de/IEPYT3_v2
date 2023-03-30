user = {"id": 100, 
        "first_name": "Thomas", 
        "age": 55, 
        "anwesend": True}


print(user, type(user))

### alternative to define a dictiony -> tbc.


# Get the value of a key
print(user["id"])
print(user["first_name"])


# print(user["car"]) # ERROR : because the 'car' does not exist
# .get() --> does not break the system if the key does not exist --> it will retrieve......
print(user.get("car"))  # None
print(user.get("car", "Banana"))  # Banana
print(user.get("car", "Not found"))  # Not found
print(user.get("age", "Not found"))  # 55




# Change a value of a key
user["age"] = 60
print(user)


# Add a key value pair
user["location"] = "Berlin"
print(user)

# Delete a key-value pair
user.pop("location")
print(user)


# delete a key
del user["age"]


# Store the poped item into a variable otherwise the not found message
first_name = user.pop("first_name", "banana")  # if the key exists, pop the pair and give me back the values, otherwise--> give banana back
print(user)
print(first_name)


# Check if a key exists
if "id" in user:
    print("The key exists")

print()


#######################################################
# Loop over a dictionary

user = {"id": 100, 
        "first_name": "Thomas", 
        "age": 55, 
        "anwesend": True}


for key in user.keys():
    print(key)
print()

for val in user.values():  
    print(val)
print()


for x in user:   # default---> iterate over keys
    print(x)
print()

for item in user.items():    # item Tuple: (key, value)
    print(item)
print()

# Unpacking of the item tuple
for key, val in user.items():    # item Tuple: (key, value)
    print(key, val)
