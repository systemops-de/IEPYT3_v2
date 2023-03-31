import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


""" 
Mode:
~~~~
w: write
a: append
"""


# You need to close the file at the end

file = open("file1.txt", mode = "a")
file.write("Hallo Thomas\n")
file.close()


# Better alternative  -> will be closed automatically
with open("file1.txt", mode = "a", encoding= "UTF-8") as file:
    file.write("Hallo Ingo\n")
    file.write("Übungen\n")
  
