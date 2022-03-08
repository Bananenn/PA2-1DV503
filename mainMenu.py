from queries import *

while True:
    mainMenu = """
    1. Select a race and the names of the pole positions will be shown. (skriv bättre)
    2. Who has participated in the most amount of races.
    3. Who has won the most amount of competitions.
    4. Avrage age of the person winning a race
    5. ...
    q. to quit
    """

    print(mainMenu)

    selected = input("Please enter a menu number: ")

    if (selected == "1"):
        podiumPlacesForRace()
    elif (selected == "2"):
        whoHasParticipatedMostRaces()
    elif (selected == "3"):
        mostWins()
    elif (selected == "4"):
        avrageAgeOfWinner()
    elif (selected == "5"):
        print("Do 5")
    elif (selected == "q"):
        print("User want to quit")
    else:
        print("Input error")