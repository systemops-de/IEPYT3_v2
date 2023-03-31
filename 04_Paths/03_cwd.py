from pathlib import Path 
import os

print("Original CWD",Path.cwd() ) # C:\Users\M
print(__file__ , type(__file__))


application_folder = Path(__file__).parent
print(application_folder) # c:\Users\M\Desktop\Python1\04_Paths


# Change the cwd to the application folder
os.chdir(application_folder)

print("Changed CWD",Path.cwd() ) # c:\Users\M\Desktop\Python1\04_Paths


##################################################
# IMMMER WENN DU MIT DATEIEN ARBEITEST
# BITTE im ERSTEN FILE--> KOPIERE FOLGENDEN LINES
# BITTE ALLE PATHS IN THE PROGRAM AS RELATIVE PATHS WITH / (pathlib)

import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)