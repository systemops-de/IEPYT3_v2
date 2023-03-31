import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


# Constants and Paths
APP_FOLDER = Path.cwd()    # c:\Users\M\Desktop\Python1\04_Paths
DATA_FOLDER = APP_FOLDER / "data"




# Get all files with txt extension in a list
list_of_files = list(DATA_FOLDER.rglob("*.txt")) # rglob : recusive glob ---> also of sub folders
print(list_of_files)

print()

# Iterate and show the files 
for file in list_of_files:
    print(file)
