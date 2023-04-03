# PDF Merging 
""" 
in Terminal:

> pip install pypdf2
> pip install   --proxy=http://proxywbs:3128    pypdf2
> pip install   --proxy=http://proxywbs:3128    ipykernel

"""

import os
from pathlib import Path

from PyPDF2 import PdfMerger

os.chdir(Path(__file__).parent)


# 1. List of PDF Files
pdfs = ["T1.pdf", "T2.pdf", "T3.pdf"]


# 2. Create a merger (instance)
merger = PdfMerger() 

# 3. Loop over files
for pdf in pdfs:
    merger.append(pdf)


# 4. Write the result pdf
merger.write("combined.pdf")
