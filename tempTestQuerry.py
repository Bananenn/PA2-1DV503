
# You will need to use the Connector/Python
from re import I
import mysql.connector

# From slides
cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1')
myCursor = cnx.cursor()

# Your code should check if the database with your last name exists
# If the database does not exist, it should be created
myCursor.execute("USE GoKart")

def listRacesAndPick():
    myCursor.execute("SELECT DISTINCT race_name,date FROM races")
    result = myCursor.fetchall()
    i = 0
    for race in result:
        i += 1
        print("%d. %s %s " % (i,race[0],race[1]))

    selected = input("Select a race: ")
    print("Selected race is " + str(result[int(selected)-1]))


listRacesAndPick()