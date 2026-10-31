# Library Management System

A command-line application built with Python and MySQL to store and manage books.

## Features
- Add books with a title, author, and category.
- Display all saved books.
- Search for books by title.
- Validate empty fields and handle database errors.

## Files
- main.py: Python application.
- database.sql: Creates the database and books table.

## How to Run
1. Install Python and MySQL Server.
2. Run database.sql in MySQL Workbench.
3. Install the connector: `python -m pip install mysql-connector-python`
4. Run the application: `python main.py`
5. Enter your MySQL root password when prompted.

Books are saved in MySQL and remain available after closing the application.
