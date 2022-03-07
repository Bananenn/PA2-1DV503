# You will need to use the Connector/Python
from ast import match_case
import queue
from sqlite3 import Cursor
from ssl import match_hostname
import mysql.connector
from csv import reader

# From slides
cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1')
myCursor = cnx.cursor()
myCursor.execute("USE GoKart")

def stringCleaner(string):
  clean = str(string).replace("('", "").replace("',)", "").replace("'", "").replace(")", "").replace('"', "").replace(",", "").replace("(", "")
  return clean


def podiumPlacesForRace(mycursor):
  raceDetails = listRacesAndPick()
  mycursor.execute("""
    SELECT participant.name, scoreboard.placing
    FROM gokart.participant  
    INNER JOIN gokart.scoreboard  
    ON participant.id = scoreboard.participant_id
    WHERE scoreboard.race = "%s" AND scoreboard.date = "%s" AND scoreboard.placing <= 3
    ORDER BY scoreboard.placing
    """ % (raceDetails[0], raceDetails[1]))
  
  print("\n" + ("—") * 29)  
  print("Podium places for %s" % raceDetails[0])
  print("—" * 29)  
  print("| {:20} | {:2} |".format("Name", "#"))
  print("—" * 29)
  for (name, placing) in mycursor:
    print("| {:20} | {:2} |".format(name, placing))
  print("—" * 29)

#Example for whoWonRace()
# podiumPlacesForRace(myCursor, "Helmet Hair 2021")

def whoHasParticipatedMostRaces():
  #TODO program things she has participated in 110 races counts 6 in both tables should only count in 1
  myCursor.execute("""SELECT
  participant_id, participant.name,
  COUNT(participant_id) AS numberOfRaces 

  FROM
  gokart.scoreboard, gokart.participant

  GROUP BY 
  scoreboard.participant_id

  ORDER BY 
  numberOfRaces DESC

  LIMIT 1;""")
  
  mostParticipation = myCursor.fetchone()
  print("\n" + ("—") * 29)  
  print("%s has participated in the most races a total of %s" % (mostParticipation[1], mostParticipation[2]))#for (name, numberOfRaces) in cursor:
  print("—" * 29)

def listRacesAndPick():
    myCursor.execute("SELECT DISTINCT race_name,date FROM races")
    result = myCursor.fetchall()
    i = 0
    for race in result:
        i += 1
        print("%d. %s %s " % (i,race[0],race[1]))

    selected = input("Select a race: ")
    print("Selected race is " + str(result[int(selected)-1]))
    return result[int(selected)-1]

def mostWins():
  querry = """
  SELECT participant.name, COUNT(participant.name) AS numOfWins
  FROM gokart.participant  
  INNER JOIN gokart.scoreboard  
  ON participant.id = scoreboard.participant_id
  WHERE placing=1
  GROUP BY participant.name
  ORDER BY numOfWins DESC
  LIMIT 1;
  """
  myCursor.execute(querry)
  mostWins = myCursor.fetchone() # - Since limit is 1 anyway no need to "fetch all"
  print("%s has won the most amount or faces with a total of %s" % (mostWins[0], mostWins[1]))


whoHasParticipatedMostRaces()