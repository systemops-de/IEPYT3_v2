# Pathlib : Modern , standard library in python

from pathlib import Path 


# string
file_path = "C:\\Python\\Python3112\\"  
file_path = r"C:\Python\Python3112"  


file_path = "C:/Python/Python3112"   # format of Linux, MAC

# create an intelligent Path from a string  -> it also convert the path to the right format (using \ or /)
file_path = Path(file_path)

print(file_path, type(file_path)) # C:\Python\Python3112

# Concate the paths using / (without os.path.join)
file_path = file_path / "names.txt"
print(file_path) # C:\Python\Python3112\names.txt



### Via the intelligent Path object -> we have a lot of benefits, some of them: 

print(file_path.name) # names.txt
print(file_path.suffix) # .txt
print(file_path.stem) # names

# Check of the file exists
if file_path.exists():
    print("The files exists")
else:
    print("The file does not exist")


# Show the Parents of a path 
print(file_path.parent) # C:\Python\Python3112
print(file_path.parent.parent) # C:\Python
print(file_path.parent.parent.parent) # C:\


print(file_path.parents[1]) # C:\Python
print(file_path.parents[2]) # C:\

print(file_path.parts) # ('C:\\', 'Python', 'Python3112', 'names.txt')
print()

###############################################
# Current working directory : Is the entry point to the python interpreter
print(Path.cwd()) # current working directory


# Absolute Path
file_to_open = "D:/application1/text1.txt"


# Relative Path
""" 
. : current folder
.. : one level up
"""
file_to_open = "./Application_Folder/text1.txt"
file_to_open = "../Application_Folder/text1.txt"
file_to_open = "../../Application_Folder/text1.txt"  # two levels up