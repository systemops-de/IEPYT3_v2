# Summary

## Naming in Python

- num: variable (of normal value or address of function/object/class/etc.)
- num(): function
- num[]: indexing
- .num(): method
- NUM: Constant
- Num: Class
___
## Mutable and Immutable Data Types
### Immutable Data Types: 
containers which the original container can NOT be modified, a new address will be created

- int
- float
- str
- bool
- tuple
- frozenset

### Mutables: 
containers which the original container can be modified 
- list
- dict
- set
- bytearray
___

## Change Working Directory within Python
add the following codes in the first python file or config file module
~~~python
import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)
~~~
___
## Pip (Package Installer)

- Some pip commands:
~~~bash
> pip --version
> pip list
> pip show pypdf2 
> pip install pypdf2
> pip uninstall pypdf2

> pip freeze > requirements.txt
> pip install -r requirements.txt
~~~

- pip with proxy
~~~bash
> pip install --proxy=http://proxywbs:3128 ipykernel
> pip install --proxy=http://proxywbs:3128 pypdf2
~~~

- pip without proxy
~~~bash
> pip install ipykernel
> pip install pypdf2
~~~

___
## Compileall

~~~bash
>python -m compileall  app.py  app2.py   --> specific files
>python -m compileall                    --> all files
~~~


## VirtualEnv

For windows:
~~~bash
# Create myenv 
> python -m venv myenv  (Winows)

# Activate the myenv
> .\myenv\Scripts\activate

# Deactivate
> deactivate
~~~

If the Windows Policy blocks activating the virtualenv, then you need to allow it. scope here is just for this terminal (process). But you can allow it on the user/local machine level.

For more about it: 
https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/set-executionpolicy?view=powershell-7.3

~~~bash
Set-ExecutionPolicy Unrestricted -Scope Process
~~~


## Structure eines Programs:
General folder structure, it may differ from project to project

1. src: where the application real source code
2. test: where the testing source code
3. docs: auto-generated software documentation
4. assets: (images, logos, videos,styles, etc.)
5. READMe.md: how the application works, guidance, etc.
6. requirements.txt

Other Software Engineering files/deployment files (depend on the technology stack of the project), such as:
1. Docker files
2. Config files
3. Deployment files
4. License
5. Certificates
6. etc.



## Code Runner:
- Preserve Focus (uncheck)
- Run In Terminal (check)
- Save File Before Run (check)