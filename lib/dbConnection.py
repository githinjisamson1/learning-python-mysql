
# !import the connector/module
import mysql.connector

# !MySQL server details
host = "localhost"
user = "root"
password = "$Samsongithinji2019"
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

# !Creating an instance of 'cursor' class
# which is used to execute the 'SQL'
# statements in 'Python'
cursor = mydb.cursor()

# !Creating a database with a name
''''
sample_db' execute() method
is used to compile a SQL statement
below statement is used to create
the 'sample_db' database
'''
# cursor.execute("create database sample_db")

# !check databases created
# cursor.execute("show databases")

# !iterate databases created
# for item in cursor:
#     print(item)

# !create a table
# cursor.execute('''create table sample_table(
#     id int auto_increment primary key,
#     first_name varchar(255) not null,
#     last_name varchar(255) not null
#     )''')

# !check tables created
cursor.execute("show tables")

# !iterate tables created
for item in cursor:
    print(item)

# !alter
# cursor.execute("ALTER TABLE sample_table MODIFY COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# !drop
# cursor.execute("drop table sample_table")

# !insert single item
sql = "INSERT INTO sample_table (first_name, last_name) VALUES (%s, %s)"
val = ("John", "Doe")

# cursor.execute(sql, val)
# mydb.commit()
# print(cursor.rowcount, "record inserted.")

# !insert many items
sql = "INSERT INTO sample_table (first_name, last_name) VALUES (%s, %s)"
val = [
    ('Peter', 'Lowstreet 4'),
    ('Amy', 'Apple st 652'),
    ('Hannah', 'Mountain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean blvd 2'),
    ('Betty', 'Green Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lane 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]

# cursor.executemany(sql, val)
# mydb.commit()

# !rowcount/lastrowid
# print(cursor.rowcount, "records were inserted.")
# print(cursor.lastrowid, "is the last record Id")

# !select from a table
# cursor.execute("SELECT * FROM sample_table")
# cursor.execute("SELECT first_name FROM sample_table")
# cursor.execute('''SELECT * FROM sample_table WHERE first_name="John"''')
cursor.execute('''SELECT * FROM sample_table WHERE first_name LIKE "%ett%"''')

# fetch all rows from last executed statement
recordsReturned = cursor.fetchall()
# recordReturned = cursor.fetchone()

# iterate
for item in recordsReturned:
    print(item)
    
# print(recordReturned)
    
    
