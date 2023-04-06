# pip install ruamel.yaml 
# pip install yaml
""" 
Friendly Human Readable Data Format

-- YAML is not Standard in Python
-- Depened on external libraries
-- It is not always avaialbe in all technolgies
-- 
"""
import os
from pathlib import Path

os.chdir(Path(__file__).parent)



from ruamel.yaml import YAML

with open("./user.yaml", mode = "r", encoding= "UTF-8") as file:
    content = file.read()

print(content)

yaml_reader = YAML() 

yaml_data = yaml_reader.load(content)


print(yaml_data, type(yaml_data))


print(yaml_data["first_name"])
print(yaml_data["teilnehmende"])