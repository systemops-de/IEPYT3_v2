# Old school , standard original wayy

import os.path 


# Mac, Linux
file_path = "home/desktop/thomas/"

# Windows Path
file_path = "C:\\Python\\Python3112\\"

file_path = r"C:\Python\Python3112\names.txt"


file_path = r"C:\Python" + r"\Python3112" + r"\name.txt"
print(file_path)



folder_path = os.path.join("c:", "python", "python3112")
print(folder_path)  # c:python\python3112


file_path = os.path.join(folder_path, "names.txt")
print(file_path) # c:python\python3112\names.txt


"""
__file__    : the absolute path of the current python file
"""

print(__file__)


