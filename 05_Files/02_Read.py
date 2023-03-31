import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)




# with open("file1.txt", mode = "r", encoding= "UTF-8") as file:
#     content = file.read() 

# print(content)



with open("file3.txt", mode = "r", encoding= "UTF-8") as file:
    content = file.readlines() # list of lines(strings)

print(content)