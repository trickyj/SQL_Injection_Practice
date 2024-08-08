import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)

connection = sqlite3.connect('sample.db')
# table = 'CREATE TABLE people (id integer primary key, name TEXT, surname TEXT)'

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# SQL statement to create the 'users' table
# cursor.execute(table)
# connection.commit()

# CREATE TABLE users(
#     ID INTEGER PRIMARY KEY,
#     username TEXT,
#     password TEXT,
#     Date TEXT,        -- Use TEXT for date strings
#     Ranking INTEGER,
#     Pincode TEXT - - Use TEXT for PIN codes to handle leading zeros
# )

create_table_sql = '''
CREATE TABLE IF NOT EXISTS users (
    ID INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    Date TEXT, 
    Ranking INTEGER,
    Pincode TEXT 
); 
'''

create_employees_table = '''
    CREATE TABLE IF NOT EXISTS employees (
        EmployeeID INTEGER PRIMARY KEY,
        FirstName TEXT,
        LastName TEXT,
        HireDate TEXT,
        Salary REAL,
        DepartmentCode INTEGER
);
'''
# execute the SQL statement to create the table

cursor.execute(create_table_sql, create_employees_table)

# commit the transation to save changes

connection.commit()

# close the connection

connection.close()
