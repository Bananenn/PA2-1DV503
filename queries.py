# You will need to use the Connector/Python
from ast import match_case
import queue
from sqlite3 import Cursor
from ssl import match_hostname
import winsound
import mysql.connector
from csv import reader

# From slides
cnx = mysql.connector.connect(user='root', password='root',host='127.0.0.1')
myCursor = cnx.cursor()
myCursor.execute("USE GoKart")

def stringCleaner(string):
  clean = str(string).replace("('", "").replace("',)", "").replace("'", "").replace(")", "").replace('"', "").replace(",", "").replace("(", "")
  return clean

def podiumPlacesForRace():
  raceDetails = listRacesAndPick()
  myCursor.execute("""
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
  for (name, placing) in myCursor:
    print("| {:20} | {:2} |".format(name, placing))
  print("—" * 29)

#Example for whoWonRace()
# podiumPlacesForRace(myCursor, "Helmet Hair 2021")

def whoHasParticipatedMostRaces():
  #TODO program things she has participated in 110 races counts 6 in both tables should only count in 1
  myCursor.execute("""SELECT
    participant_id,
    COUNT(participant_id) AS numberOfRaces
    FROM
    gokart.scoreboard
    GROUP BY
    scoreboard.participant_id
    ORDER BY
    numberOfRaces DESC
    LIMIT 1""")
  
  idAndAmmount = myCursor.fetchone()
  
  myCursor.execute("""SELECT 
    participant.name
    FROM
    participant
    WHERE
    participant.id = %s;""" %idAndAmmount[0])

  who = myCursor.fetchone()[0]

  print("\n" + ("—") * 59)  
  print("%s has participated in the most races a total of %d" % (who, idAndAmmount[1]))#for (name, numberOfRaces) in cursor:
  print("—" * 59)

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
  myCursor.execute("""
  SELECT participant.name, COUNT(participant.name) AS numOfWins
  FROM gokart.participant  
  INNER JOIN gokart.scoreboard  
  ON participant.id = scoreboard.participant_id
  WHERE placing=1
  GROUP BY participant.name
  ORDER BY numOfWins DESC
  LIMIT 1;
  """)
  mostWins = myCursor.fetchone() # - Since limit is 1 anyway no need to "fetch all"
  print("\n" + ("—") * 73) 
  print("%s has won the most amount of races with a total of %s victories!" % (mostWins[0], mostWins[1]))
  print("—" * 73)

def avrageAgeOfWinner():
  myCursor.execute("""
  SELECT avg(age)
  FROM goKart.participant
  INNER JOIN goKart.scoreboard ON participant.id=scoreboard.participant_id AND placing = 1
  """)
  avrAge = myCursor.fetchone()[0] # - Since limit is 1 anyway no need to "fetch all"
  print("\n" + ("—") * 30) 
  print("The avrage are of the person winning a race is %s" % avrAge)
  print("—" * 30)

def kartColor4thPlace():
  myCursor.execute("""
  SELECT carts.color AS cart_color,
  COUNT(cart_id) AS cart_count
  FROM gokart.scoreboard
  LEFT JOIN gokart.carts ON cart_id = carts.no
  WHERE scoreboard.placing = 4
  GROUP BY carts.color
  ORDER BY cart_count DESC
  LIMIT 1
  """)
  color = myCursor.fetchone()
  print("\n" + ("—") * 80) 
  print("%s is the most common cart-color for all the fourth places with %d occurrences." % (str(color[0]).capitalize(), color[1]))
  print("—" * 80)

def engineSizeWinnerLooserHelmetHair():
  myCursor.execute("""
  SELECT 
    scoreboard.placing, carts.engine_size
  FROM
    gokart.scoreboard
        LEFT JOIN
    gokart.carts ON cart_id = carts.no
  WHERE
    (scoreboard.race = "Helmet Hair 2021" AND scoreboard.placing = 1) OR (scoreboard.race = "Helmet Hair 2021" AND scoreboard.placing = 8)
  ORDER BY placing ASC
  LIMIT 2
  """)
  winnerLoser = myCursor.fetchall()

  print("\n " + ("—") * 96)
  for each in winnerLoser:
    if each[0] == "1":
      print("| {:93} | ".format("The winner in Helmet Hair 2021 used a kart with " + each[1] + " cc engine size."))
    elif each[0] == "8":
      print("| {:93} |".format("The person that came in last place in Helmet Hair 2021 used a kart with " + each[1] + " cc engine size."))
  print(" " + ("—") * 96)

