
# Databases
# Setup PostgreSQL
# Read data
# Load data
# Modify data

# PostgreSQL https://www.postgresql.org/download/
# https://www.enterprisedb.com/downloads/postgres-postgresql-downloads

# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
# https://docs.sqlalchemy.org/en/13/dialects/
# https://docs.sqlalchemy.org/en/13/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg2

import psycopg2

orskl_connect = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "localhost",
                                  port = "5432",
                                  database = "postgres")

orskl_cursor = orskl_connect.cursor()
orskl_cursor.execute("select version()")
orskl_output = orskl_cursor.fetchall()


orskl_cursor.execute('''CREATE TABLE students
          (id INT PRIMARY KEY     NOT NULL,
          name           TEXT    NOT NULL,
          location         TEXT) ''')
orskl_connect.commit()

orskl_connect.commit()
orskl_cursor = orskl_connect.cursor()
orskl_insert = """INSERT INTO students (id, name, location) VALUES (%s, %s, %s)"""
orskl_data = (1003, 'Student 1', 'India')
orskl_cursor.execute(orskl_insert , orskl_data)
orskl_connect.commit()
orskl_connect.commit()
orskl_cursor.execute('''INSERT INTO students (id, name, location) VALUES (1004, 'Student 2', 'USA')''')
orskl_connect.commit()

orskl_cursor = orskl_connect.cursor()
orskl_select = orskl_cursor.execute('select * from students')
orskl_select_data = orskl_cursor.fetchall()
print(orskl_select_data)

import pandas as pd
from sqlalchemy import create_engine

orskl_engine = create_engine(
    "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
    user = 'postgres',
    password = 'postgres',
    host = 'localhost',
    port = 5432,
    database = 'postgres',
)
)

df = pd.read_sql_table('students', con=orskl_engine)
print(df)
df2 = pd.DataFrame(
    {
        'id' : [1007, 1005, 1006],
        'name' : ['Student 3', 'Student 4', 'Student 5'],
        'location': ['USA' ,'UAE','UK']
    }
)
df2.to_sql('students', con=orskl_engine, if_exists='append', index=False)



import psycopg2
try:
    orskl_connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "localhost",
                                  port = "5432",
                                  database = "postgres")

    orskl_cursor = orskl_connection.cursor()
    # Print PostgreSQL Connection properties
    print (orskl_connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    orskl_cursor.execute("SELECT version();")
    orskl_record = orskl_cursor.fetchone()
    print("You are connected to - ", orskl_record,"\n")

except (Exception, psycopg2.Error) as orskl_error :
    print ("Error while connecting to PostgreSQL", orskl_error)
finally:
    #closing database connection.
        if(orskl_connection):
            orskl_cursor.close()
            orskl_cursor.close()
            print("PostgreSQL connection is closed")



import psycopg2
try:
    orskl_connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")

    orskl_cursor = orskl_connection.cursor()

    create_table = '''CREATE TABLE students
          (id INT PRIMARY KEY     NOT NULL,
          name           TEXT    NOT NULL,
          location         TEXT); '''

    orskl_cursor.execute(create_table)
    orskl_connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error while creating PostgreSQL table", error)
finally:
    # closing database connection.
    if (orskl_connection):
        orskl_cursor.close()
        orskl_connection.close()
        print("PostgreSQL connection is closed")



import psycopg2

try:
    orskl_connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
    orskl_cursor = orskl_connection.cursor()
    insert_query = """ INSERT INTO students (id, name, location) VALUES (%s,%s,%s)"""
    record1 = (1002, 'Student 1', 'India')
    orskl_cursor.execute(insert_query, record1)

    orskl_connection.commit()
    rows = orskl_cursor.rowcount
    print (rows, "Record inserted successfully into mobile table")
except (Exception, psycopg2.Error) as error :
    if(orskl_connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(orskl_connection):
        orskl_cursor.close()
        orskl_connection.close()
        print("PostgreSQL connection is closed")




try:
    orskl_connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")
    orskl_cursor = orskl_connection.cursor()
    select_Query = "select * from students"

    orskl_cursor.execute(select_Query)
    print("Selecting rows from mobile table using cursor.fetchall")
    data = orskl_cursor.fetchall()

    print("Print each row and it's columns values")
    for row in data:
        print("id = ", row[0], )
        print("name = ", row[1])
        print("location  = ", row[2], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if (orskl_connection):
        orskl_cursor.close()
        orskl_connection.close()
        print("PostgreSQL connection is closed")



import pandas as pd
from sqlalchemy import create_engine

# follows django database settings format, replace with your own settings
orskl_postgres = {
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': 5432,
}

orskl_engine = create_engine(
    "postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}".format(
    user = orskl_postgres['USER'],
    password = orskl_postgres['PASSWORD'],
    host = orskl_postgres['HOST'],
    port = orskl_postgres['PORT'],
    database = orskl_postgres['NAME'],
)
)


# read a table from database into pandas dataframe, replace "tablename" with your table name
df = pd.read_sql_table('students',orskl_engine)
df2 = pd.DataFrame({'id' : [1002, 1003, 1004, 1005],
       'name': ['Student 2', 'Student 3', 'Student 4', 'Student 5'],
       'location' : ['India', 'USA', 'UK', 'UAE']
       })
df2.to_sql('students', con=orskl_engine, if_exists='append', index=False)
df = pd.read_sql_table('students',orskl_engine)

