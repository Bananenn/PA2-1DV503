#Q Vem vann Mouce race (1a 2a 3e plats)
"""
SELECT participant.name, scoreboard.placing
FROM gokart.participant  
INNER JOIN gokart.scoreboard  
ON participant.id = scoreboard.participant_id
WHERE scoreboard.race = "Mouse race" AND scoreboard.placing <= 3
ORDER BY scoreboard.placing
"""

#Q: Who has participated in the most amount of races
#WARNING! Om två eller flera deltagit i samma antal races vet i fan hur det bestäms vem 
""""
SELECT
  participant_id,
  COUNT(participant_id) AS numberOfRaces 

FROM
  gokart.scoreboard

GROUP BY 
  scoreboard.participant_id

ORDER BY 
  numberOfRaces DESC

LIMIT 1;
"""

#Q: Who has won the most amount of competitions?
#WARNING! Om två eller flera deltagit i samma antal races vet i fan hur det bestäms vem 
"""
SELECT
  participant.name,
  COUNT(participant.name) AS numOfWins

FROM gokart.participant  
INNER JOIN gokart.scoreboard  
ON participant.id = scoreboard.participant_id
WHERE placing=1

GROUP BY 
  participant.name

ORDER BY 
  numOfWins DESC

LIMIT 1;
"""



