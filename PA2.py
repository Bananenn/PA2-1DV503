# You will need to use the Connector/Python
from ast import match_case
from ssl import match_hostname
import mysql.connector
from csv import reader

# From slides
cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1')
myCursor = cnx.cursor()

# Your code should check if the database with your last name exists
# If the database does not exist, it should be created
myCursor.execute("DROP DATABASE GoKart")
myCursor.execute("CREATE DATABASE IF NOT EXISTS GoKart")
myCursor.execute("USE GoKart")


def CreateTable(header, tableName):
    colums = ""
    for name in header:
        colums += ("%s varchar(255)," % name)

    colums = colums[:-1] # - Remove the last ,

    sqlQuerry = ("""
    CREATE TABLE %s (%s);
    """) % (tableName,colums)
    myCursor.execute(sqlQuerry)

def addTableContent(tableName, header, valuales):
    header = str(header).replace("[", "").replace("]", "").replace("'", "")
    valuales = str(valuales).replace("[", "").replace("]", "")
    sqlQuerry = ("""
    INSERT INTO %s (%s)
    VALUES (%s);
    """) % (tableName, header, valuales)
    myCursor.execute(sqlQuerry)
    cnx.commit() # - This is needed for it to work, Only when inserting things tho

# - For each file add table & fill it with the content from the files.   
for file in ["carts", "races","participant","scoreboard"]:
    # - Open files and get relevant info
    with open(("csvFiles/%s.csv" % file), 'r') as read_obj:
        scv_reader = reader(read_obj)
        header = next(scv_reader)
        CreateTable(header, file)
        # - surley not the best way, But i rely on next() to throw an exception when we have gone through all rows
        try:
            while True:
                addTableContent(file, header, next(scv_reader)) # next(scv_reader) will throw an excpetion
        except:
            print(" -- No more rowns for file {:13} --".format(file))



# - temp

