import time
import keyboard
from queries import *

def waitMenu():
    wait = True
    while (wait):
        time.sleep(0.1)  # Sleep to reduce button bounce
        print("\nPress any key to return to main menu.")
        if keyboard.read_key():
            wait = False

while True:
    mainMenu = """
    1. Select a race and the names of the pole positions will be shown. (skriv bättre)
    2. Who has participated in the most amount of races.
    3. Who has won the most amount of competitions.
    4. ...
    5. ...
    q. to quit
    """

    print(mainMenu)

    selected = input("Please enter a menu number: ")

    if (selected == "1"):
        podiumPlacesForRace()
        waitMenu()
    elif (selected == "2"):
        whoHasParticipatedMostRaces()
        waitMenu()
    elif (selected == "3"):
        mostWins()
        waitMenu()
    elif (selected == "4"):
        print("Do 4")
    elif (selected == "5"):
        print("Do 5")
    elif (selected == "q"):
        print("User want to quit")
    else:
        print("Input error")