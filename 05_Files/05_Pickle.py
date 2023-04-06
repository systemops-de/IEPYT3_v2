import os
import pickle
from pathlib import Path

os.chdir(Path(__file__).parent)

""" 
modes:
~~~~~
wb: write binary
rb: read binary
"""

message  = """
Hallo Thomas
wie geht es dir?
schöne Grüße
Lena
"""

x = 10 



# Store the X variable from memory to a file on the harddisk
with open("./variable.pkl", mode = "wb") as file:
    pickle.dump(message, file)

x = 12

# Load a pickle from physical file to the memory again
with open("./message.pkl", mode = "rb") as file:
    myvalue = pickle.load(file)

print(myvalue)