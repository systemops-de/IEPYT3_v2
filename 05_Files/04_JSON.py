import json 
import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)

# JSON is a stricted Dictionary File FOrmat

user = {
    "id": 100,
    "name" : "Thomas",
    "kids" : {
        "0": {"id": 100, "first_name": "Julia"},
        "1": {"id": 101, "first_name": "Sara"}
    }
}


# READ the json file and convert it to Python dictionary
with open("user.json", mode = "r", encoding= "UTF-8") as file:
    content = file.read()  # string 


# Convert the string to python dict
mydict = json.loads(content)
print(mydict, type(mydict))



# Althernative:::: BETTER -> direct from file to dict
with open("user.json", mode = "r", encoding= "UTF-8") as file:
    mydict2 = json.load(file)

print(mydict2)

# Do some changes
mydict2["location"] = "Berlin"

#######################################################
# Convert the intelligent dictionary to string (JSON string)
json_str = json.dumps(mydict2)  
print(json_str, type(json_str))

with open("user2.json", mode = "w", encoding= "UTF-8") as file:
    file.write(json_str)