#!/usr/bin/env python
#
# Test cases for tournament.py


from tournament import *
import psycopg2
import os
import re


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def newPlayer():
    clear()
    name = input("Please enter the new player's name: ")
    # This will call a function to be written later
    # checkName(name)
    try:
        registerPlayer(name)
    except:
        print "there was an error registering you as a player"
    cur.execute("select * from players where name = " + name)
    output = cur.fetchall()
    print """
    
    This is your player information (ID#, Name, Wins, Matches)
    """ + output + """
    This information will be used for tournament purposes
    """
    input("Press <ENTER> to continue...")
    clear()
    main()


def checkname(name):
    """
    This will eventually be able to check names to see if they have
    any special characters. Valid characters will include Letters
    both lowercase and capital, spaces for players who wish to have
    their first and last name listed, and apostrophies for players
    like "Boots O'Neal" who like to through things off.
    """
    
    clear()
    
def killplayer()
    """
    This will enable a user to delete a player from the tournament
    database. This will require a user to know the playerid of the
    person they are attempting to delete. 

    First see if the user has the playerid of the person they are
    trying to delete. If they do then great enter it and present
    the player information with one last confirm to delete the player

    If the user does not have the playerid of the person they are trying
    to delete they will have to select from a new menu and enter
    the information that they do have
    """
    
    clear()
    inp = input("""
    Do you know the player id number of the player you would like to delete?
                """)
    inp = inp.lower()
    if inp == "y" | inp == "yes":
        clear()
        print """Awesome in that case please enter it below
        
        """
        inp = input("Player ID number: ")
        # at this point code will continue outside the if statement
    else:
        """
        if the user does not have the player's id number then they will need
        to perform a search to get the information
        playerSearch()
        For now playerSearch() is not really a function, but later it will
        allow for a user to actually select which information they have
        and search by that, or show all players currently enrolled in the
        current database
        """

def deletePlayer(playerid)
    """ Takes player id from user and deletes the player """
    # fetch and display the user based on the ID number entered
    cur.execute("select * from players where playerid = " + str(inp))
    ouput = cur.fetchall()
    print """Is this the player that you would like to delete?
    
    """ + output + """
    
    [yes / no]
    """
    inp = input("")
    if inp.lower == "y" | inp.lower == "yes":
        cur.execute("delete * from players where playerid = " + playerid)
        conn.commit()
    else:
        clear()
        print """
        I'm sorry, I did not understant your command...
        
        Please press <ENTER> to return to the main screen...
        """
        input("")