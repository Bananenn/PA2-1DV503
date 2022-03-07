# You will need to use the Connector/Python
from ast import match_case
from ssl import match_hostname
import mysql.connector
from csv import reader

# From slides
cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1')
myCursor = cnx.cursor()

def stringCleaner(string):
  clean = str(string).replace("('", "").replace("',)", "").replace("'", "").replace(")", "").replace('"', "").replace(",", "").replace("(", "")
  return clean


def podiumPlacesForRace(mycursor, race):
  mycursor.execute("""
    SELECT participant.name, scoreboard.placing
    FROM gokart.participant  
    INNER JOIN gokart.scoreboard  
    ON participant.id = scoreboard.participant_id
    WHERE scoreboard.race = "%s" AND scoreboard.placing <= 3
    ORDER BY scoreboard.placing
    """ % race)
  
  print("\n" + ("—") * 29)  
  print("Podium places for %s" % race)
  print("—" * 29)  
  print("| {:20} | {:2} |".format("Name", "#"))
  print("—" * 29)
  for (name, placing) in mycursor:
    print("| {:20} | {:2} |".format(name, placing))
  print("—" * 29)

#Example for whoWonRace()
# podiumPlacesForRace(myCursor, "Helmet Hair 2021")

def whoHasParticipatedMostRaces(cursor):
  cursor.execute("""SELECT
  participant_id, participant.name,
  COUNT(participant_id) AS numberOfRaces 

  FROM
  gokart.scoreboard, gokart.participant

  GROUP BY 
  scoreboard.participant_id

  ORDER BY 
  numberOfRaces DESC

  LIMIT 1;""")
  
  mostParticipation = cursor.fetchone()
  print("\n" + ("—") * 29)  
  print("%s has participated in the most races a total of %s" % (mostParticipation[1], mostParticipation[2]))#for (name, numberOfRaces) in cursor:
  print("—" * 29)

whoHasParticipatedMostRaces(myCursor)