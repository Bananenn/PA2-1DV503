# Programming assignment 2 - Database Technology, 1DV503
#
# Created by André Franzén, af223kr & Daniel Mogensen, djovy08
# March 2022
#
from queries import *

def mainMenu():
  running = True
  createView() # Creating a view to mask out the planned races that havent yet been done.
  print("\n\n***************** Welcome to the GoKartClub Fancy Racers! *****************\n*** Here you can get some information about the members and some races. ***")
  print("—" * 75)

  while running:
      mainMenu = """
      1. Select a race and the top three racers will be shown.
      2. Show who has participated in the most amount of races.
      3. Show who has won the most amount of competitions.
      4. Show the average age of the person winning a race.
      5. Show the most common color of cart for placing 4th place in races.
      6. Show the engine size of the winner and the looser in the race Helmet Hair 2021.
      q. to quit
      """
      print(mainMenu)

      selected = input("Please enter a number to navigate the menu: ")

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
          SystemExit
      else:
          print("Wrong input. Try again.")

mainMenu()