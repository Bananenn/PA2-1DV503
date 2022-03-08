from queries import *

running = True
while running:
    mainMenu = """
    1. Select a race and the names of the pole positions will be shown. (skriv bättre)
    2. Who has participated in the most amount of races.
    3. Who has won the most amount of competitions.
    4. Avrage age of the person winning a race
    5. The most common color of cart for placing 4th place.
    6. Engine size of winner and looser in the race Helmet Hair 2021.
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
        kartColor4thPlace()
    elif (selected == "6"):
        engineSizeWinnerLooserHelmetHair()
    elif (selected == "q"):
        running = False
    else:
        print("Input error")