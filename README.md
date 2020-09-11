# Desktop database application using python.

This project demonstrates a desktop application for student database. It can
1. View all entries.
2. Add a new entry.
3. Delete an existing entry.
4. Update an existing entry.
5. Search for an existing entry.

An sqlite database is created to store all the information.

## Prerequisites

Install tkinter and sqlite3 libraries using the below commands.

````
pip install tk

````

````
pip install db-sqlite3

````

## Usage

Run the python file frontend.py. Use the commands below in any terminal.

````
python frontend.py

````
or if the python version is 3, use command.

````
python3 frontend.py

````
or you can also use any python IDE.

## Converting code to desktop application

For converting the code to a stand-alone desktop application, we need pyinstaller.
You can install it using the following command.

````

pip install pyinstaller

````

Then for converting, use the below command,

````

pyinstaller --onefile --windowed frontend.py

````

You can find the frontend.exe file in dist folder created.