user = {
    "id": 100,
    "first_name" : "Thomas",
    "last_name" : "Meier",
    "age": 55,
    "cars" : ["VW" , "Audi"],
    "kids" : ["Julia", "Lena"],
    "kids2" : [ ("Julia", 22) , ("Lena" , 21)  ],
    "kids3" : [ 
                {"first_name": "Julia", "age": 22, "friends": ["Frank", "Steffi"]}  , 
                {"first_name": "Lena", "age": 21, "friends": ["Johannes"]}                    
              ],    
    "kids4" : {
               "kid1" : {"first_name": "Julia", "age": 22, "friends": ["Frank", "Steffi"]}  , 
               "kid2" : {"first_name": "Lena", "age": 21, "friends": ["Johannes"]}                  
              },
}

print(user)
print(user["first_name"])
print(user["cars"])
print(user["cars"][0])
print(user["kids"][1])

print(user["kids2"][0][0]) # "Julia"
print(user["kids2"][1][1]) # 21


print(user["kids3"][0])
print(user["kids3"][0]["first_name"]) # Julia
print(user["kids3"][0]["friends"][0]) # Frank

print(user["kids3"][1]["friends"][0])

print(user["kids4"]["kid1"]["age"]) # 22

print()
##################################################


user = {
    "id": 100,
    "first_name" : "Thomas",
    "kids3" : [ 
                {"first_name": "Julia", "age": 22, "friends": ["Frank", "Steffi"]}  , 
                {"first_name": "Lena", "age": 21, "friends": ["Johannes"]}                    
              ],       
}

# Show me all kids --> the records of kids , the dict of kids
for kid in user["kids3"]:
    print(kid)

# Show for each kid the first name
for kid in user["kids3"]:
    print(kid["first_name"])


# Show the friends (as a list) of each kid
for kid in user["kids3"]:
    print(kid["friends"])
print()

# Show for each, the listing of all friends
for kid in user["kids3"]:  # kid: is a dict
    print(kid["first_name"])
    print("~" * 10)

    for friend in kid["friends"]:  # kids["friends"] : list
        print(friend) # friend: str

    print()
    
""" 
Julia
~~~~~
Frank 
Steffi

Lena
~~~~
Johannes


"""
    