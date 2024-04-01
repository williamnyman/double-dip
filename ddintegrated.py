# going to us SQlite and pray that the SQL commands dont differ much from Postgre
# imports
import sqlite3

# connect to database
connection = sqlite3.connect("courses.db")

# open cursor to perform database operations
cursor = connection.cursor()

# populate the database
### right here i want to include something like a text file with all 
#   the create table and insert statements for the database that way 
#   i dont need like a billion lines of code                        ###


# form the query
query = ## this will change once I have Schema figured out ##

# Execute a query
cursor.execute(## query ##)

# Retrieve query results
records = cursor.fetchall()

