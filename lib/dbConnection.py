
# !pipenv install mysql-connector-python

# !import the connector/module
import mysql.connector

# !MySQL server details
host = "localhost"
user = "root"
password = "27511112086/2019"  # should be hidden
database = "sample_db"

# !establish the connection/create connection object
mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# !printing the connection object
print(mydb)

'''
!Creating an instance of 'cursor' class
which is used to execute the 'SQL'
statements in 'Python'
'''
cursor = mydb.cursor()

# !Creating a database with a name
''''
sample_db' execute() method is used to compile a SQL statement
below statement is used to create the 'sample_db' database
'''
# cursor.execute("create database sample_db")

# !check databases created
# cursor.execute("show databases")

# !iterate databases created
# for item in cursor:
#     print(item)

# !create a table
# CREATE TABLE IF NOT EXISTS sample_table
# cursor.execute('''create table sample_table(
#     id int,
#     first_name varchar(255) not null,
#     last_name varchar(255) not null
#     )''')

# !check tables created
# cursor.execute("show tables")

# !iterate tables created
# for item in cursor:
#     print(item)

# !alter
# cursor.execute("ALTER TABLE sample_table MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# !drop
# cursor.execute("drop table sample_table")
# cursor.execute("DROP TABLE IF EXISTS sample_table")

# !insert single item/use %s placeholders to prevent sql injections/mydb.commit() to effect changes
# sql = "INSERT INTO sample_table (first_name, last_name) VALUES (%s, %s)"
# val = ("John", "Doe")

# cursor.execute(sql, val)
# mydb.commit()
# print(cursor.rowcount, "record inserted.")

# !insert many items
# sql = "INSERT INTO sample_table (first_name, last_name) VALUES (%s, %s)"

# list/array of tuples
# val = [
#     ('Peter', 'Doe'),
#     ('Amy', 'Kamau'),
#     ('Hannah', 'Njoroge'),
#     ('Michael', 'Kimani'),
#     ('Sandy', 'Oloo'),
#     ('Betty', 'Otieno'),
#     ('Richard', 'Murithi'),
#     ('Susan', 'Monroe'),
#     ('Vicky', 'Miles'),
#     ('Ben', 'Gordon'),
#     ('William', 'Kimani'),
#     ('Chuck', 'George'),
#     ('Viola', 'Omar')
# ]

# cursor.executemany(sql, val)
# mydb.commit()

# !rowcount/lastrowid
# print(cursor.rowcount, "records were inserted.")
# print(cursor.lastrowid, "is the last record Id")

# !select from a table
# cursor.execute("SELECT * FROM sample_table")
# cursor.execute("SELECT first_name FROM sample_table")
# cursor.execute('''SELECT * FROM sample_table WHERE first_name="John"''')
# cursor.execute('''SELECT * FROM sample_table WHERE first_name LIKE "%ett%"''')

# fetch all rows from last executed statement
# recordsReturned = cursor.fetchall()
# recordReturned = cursor.fetchone()

# iterate
# for item in recordsReturned:
#     print(item)

# print(recordReturned)

# !prevent sql injections using %s placeholder
# sql = '''SELECT * FROM sample_table WHERE last_name = %s '''
# val = ("Kimani",)

# cursor.execute(sql, val)

# records = cursor.fetchall()
# for item in records:
#     print(item)

# !order by asc/desc
# cursor.execute("SELECT first_name, last_name FROM sample_table order by first_name asc")
# cursor.execute("SELECT first_name, last_name FROM sample_table order by first_name desc")

# records = cursor.fetchall()
# for item in records:
#     print(item)

# !delete/mydb.commit() to effect changes
# sql = "DELETE FROM sample_table WHERE first_name= %s"
# sql = "DELETE FROM sample_table" deletes all records
# val = ("Betty",)

# cursor.execute(sql, val)
# mydb.commit()

# !update/mydb.commit() to effect changes/omitting the WHERE clause updates all records
# sql = "UPDATE sample_table SET last_name = %s WHERE last_name = %s"
# val = ("Mbugua", "Kimani")

# cursor.execute(sql, val)
# mydb.commit()

# !limit/offset
# sql = '''SELECT * FROM sample_table LIMIT 2 OFFSET 2'''
# cursor.execute(sql)

# records = cursor.fetchall()
# for item in records:
#     print(item)

'''
You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.
'''
# !INNER JOIN === only shows the records where there is a match
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

# !LEFT JOIN === shows the records regardless if there is no match on right
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  LEFT JOIN products ON users.fav = products.id"


# !RIGHT JOIN === shows the records regardless if there is no match on left
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  RIGHT JOIN products ON users.fav = products.id"


# !FULL OUTER JOIN === shows the records regardless if there is no match on right/left
# very few cases
