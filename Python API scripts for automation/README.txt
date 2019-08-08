
Prerequisites
-------------
Below is a list of prerequisites that need to be in place in order to compile the final executable that will be used to change the password in the scheduler.

-> Python – latest stable windows version (currently 3.7) from https://www.python.org/downloads/windows/ - “Windows x86-64 executable installer”
----Python needs to be installed by an Administrative user with the “Add Python 3.x to PATH” as checked where 3.x is the version.

->Requests module and pyinstaller needs to be installed
----In PowerShell go to the python scripts folder: “C:\Users\Administrator\AppData\Local\Programs\Python\Python37\Scripts\”
----Run the following install: “pip install requests”
----Run the following install: “pip install pyinstaller”


Then to create the standalone executable from cmd/powershell:
# pyinstaller.exe --onefile .\PasswordReconcileAPI.py