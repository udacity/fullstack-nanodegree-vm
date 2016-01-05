#!/usr/bin/env python
#
# Test cases for tournament.py


from tournament import *
import psycopg2
import os
import re


psql = psycopg2
conn = psql.connect("dbname='tournament'")
cur = conn.cursor()


def quitscreen():
    clear()
    quit()


def main():
    """ This will be the main class presented to the user.
    This is the main menu, from here the user will be able to select
    from a number of options using the numbers on their keyboard.
    """
    clear()
    print """
    1. Register a new player
    2. Delete a player *need playerid
    3. Search player information
    4. Set and display a new round
    5. Report match
    6. Delete match
    7. Search match information
    8. Get current standings
    99. Quit application

    Make your selection by entering a number...
    """
    inp = raw_input(" ")
    # Take user input and cheack againsta available options
    try:    
        if inp == "1":
            newPlayer()
        elif inp == "2":
            killplayer()
        elif inp == "3":
            searchPlayers()
        elif inp == "4":
            newRound()
        elif inp == "5":
            finishedMatch()
        elif inp == "6":
            deleteMatch()
        elif inp == "7":
            searchMatches()
        elif inp == "8":
            rankings()
        elif inp == "99":
            quitscreen()
        elif inp == "developer":
            devops()
        else:
            print "I'm sorry but that input is unrecognized..."
            raw_input("Please press <ENTER> to continue to the main screen...")
            main()
    except:
        quit()


    """
    Additional developer options to add later:
    * add 10 players with random names
    * run tournament with all players in the database
    * automated rounds
    * automated tournaments

    Possible additional user front end cases include:
    * ability to run multiplel tournaments
    """
    
    
def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def newPlayer():
    clear()
    name = str(raw_input("Please enter the new player's name: "))
    # This will call a function to be written later
    # name = checkName(name)
    print "Trying to create player : " + name
    try:
        registerPlayer(name)
    except:
        print "there was an error registering you as a player"
    name = checkName(name)
    cur.execute("select * from players where name = '" + name + "'")
    output = cur.fetchall()
    print """
    
    This is your player information (ID#, Name, Wins, Matches)
    """ + str(output) + """
    This information will be used for tournament purposes
    """
    raw_input("Press <ENTER> to continue...")
    clear()
    main()



    
def killplayer():
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
    inp = raw_input("""
    Do you know the player id number of the player you would like to delete?
    """)
    inp = inp.lower()
    try:
        if inp[0] == "y":
            clear()
            print """Awesome in that case please enter it below

            """
            inp = raw_input("Player ID number: ")
            playerid = str(inp)
            # at this point code will continue outside the if statement
        else:
            """
            If the user does not have the player's id number then they will need
            to perform a search to get the information
            """
            searchPlayers()
            """
            For now playerSearch() is not really a function, but later it will
            allow for a user to actually select which information they have
            and search by that, or show all players currently enrolled in the
            current database
            """
    except:
        """ print "Error 69, user pressed enter and left a dead string"
        print "Press <ENTER> to return to main screen..."
        raw_input("")
        main() """

    deletePlayer(playerid)


def deletePlayer(playerid):
    """ Takes player id from user and deletes the player """
    # fetch and display the user based on the ID number entered
    cur.execute("select * from players where playerid = " + playerid)
    output = cur.fetchall()
    print """Is this the player that you would like to delete?
    
    """ 
    for row in output:
        print row
    print """
    
    [yes / no]
    """
    inp = raw_input("")
    if inp[0] == "y":
        #playerid = raw_input("""What is the playerid you would like to delete?""")
        query = "delete from records where winner = %s or loser = %s;"
        data = (playerid, playerid)
        print "Test point 1"
        cur.execute(query, data)
        conn.commit()
        print "Test point 2"
        query = "delete from matches where pid1 = %s or pid2 = %s"
        data = (playerid, playerid)
        print "Test point 3"
        cur.execute(query, data)
        conn.commit()
        query = "delete from players where playerid = %s;"
        data = str(playerid)
        print "Test point 4"
        cur.execute(query, data)
        conn.commit()
        print "Test point 5"
        # cur.execute("delete from players where playerid = " + playerid)
        #conn.commit()
        main()
    else:
        clear()
        print """
        I'm sorry, I did not understant your command...
        
        Please press <ENTER> to return to the main screen...
        """
        raw_input("")
        main()


def searchPlayers():
    """ 
    This function will allow a user to search by name to find a players
    information, or they can choose to display all players information
    """
    clear()
    print "Do you wish to display all players and their information?"
    inp = raw_input("[yes / no]")
    if inp[0] == "y":
        cur.execute("select * from players order by playerid asc")
        output = cur.fetchall()
        # output = cur.mogrify(output)
        # print output
        for row in output:
            print row
    else:
        print "Error number 420."
    
    print "Press <ENTER> to return to the main screen..."
    raw_input("")
    main()

def newRound():
    """
    Create and display a new round of matches
    """
    # print swissPairings()
    matches = swissPairings()
    # there should be matches equal to the number of players divided by 2
    rows = 0
    pairs = countPlayers() / 2
    print "Here is the list of matches"
    for row in matches:
        print row
    print "Press <ENTER> to continue..."
    raw_input("")
    cur.execute("delete from matches where mid > 0")
    conn.commit()
    main()


def finishedMatch():
    """
    Create a record of each match. this will store the matchID, winnner's 
    playerID, and the loser's playerID. 

    At a later date this table may also contain the tournament ID for
    the tournament it was in, and which round of that tournament
    """
    clear()
    print """This is for creating a record of each match.
             To use this function you will need the playerid of both players
             """
    winner = raw_input("Enter the winner's PlayerID:  ")
    loser = raw_input("Enter the loser's PlayerID:  ")
    cur.execute("select playerid, name from players where (playerid = "
                + str(winner) + " or playerid = " + str(loser) + ")")
    output = cur.fetchall()
    print """You have selected the winner as
    """
    print output[0]
    print """And the loser as 
    """
    print output[1]
    print """
    
            Is this correct?
            """
    inp = raw_input("[ yes / no ]  ")
    if inp[0] == 'y':
        reportMatch(winner,loser)
        cur.execute("insert into records (winner,loser) values ("
                    + str(winner) + "," + str(loser) + ")")
        conn.commit()
        cur.execute("select * from records order by matchid desc")
        output = cur.fetchone()
        print output
        print "Press <ENTER> to return to the main screen..."
        raw_input("")
        main()
    else:
        print "ERROR incorrect info..."
        raw_input("Press <ENTER> to return to the main screen...")
        main()

        # Later i need to add checks for other inputs in the case of user error
        # also allow for blank link enter


def deleteMatch():
    """
    This will allow a user to see a list of matches to select a match ID
    Or simply enter the match ID and view the selection before deletion
    """
    matchid = "0"
    clear()
    print '''
    Woudl you like to display a list of matches?
    '''
    inp = raw_input(" [ yes / no ] ")
    if inp[0] == 'y':
        # displayMatches()
        # Function does not exist ... yet
        cur.execute("select * from records order by matchid")
        output = cur.fetchall()
        # print output
        for row in output:
            print row
        print """ Select the match id from the first column of the
        game that you would like to delete."""
        raw_input("Enter the match ID:  ")
    elif inp[0] == 'n':
        print """
        Please enter the match ID that you would like to delete:  
        """
        inp = raw_input("Match ID:  ")
        # get user input and select a match with that ID number


def devops():
    """
    This will define the developer menu used to test the application
    """
    print """
    1. Insert n players, players will have random names and be assigned no matches
    2. Test run a round
    3. Test run and display final results of tournament
    sql open an SQL Query prompt
    main  Return to main screen
    """
    opt = raw_input("Make a selection:  ")
    # get user input for option and run function
    try:
        if opt == "1":
            # run function to ask how many and insert players
            newTestPlayers()
        elif opt == "2":
            # run a test round getting matches and selecting a random winner
            testRound()
        elif opt == "3":
            # run a complete tournament using all players and display the results
            testTournament()
        elif opt == "sql":
            # open the sql prompt
            sql_cmd()
        elif opt == "main":
            # return to main screen
            main()
        
    except:
        # print "There was an error.. Press <ENTER> to return to main screen..."
        # raw_input("")
        main()
        
def sql_cmd():
    query = raw_input("""Please enter yout SQL command here:
    >>    """)
    if len(query) == 0:
        print("you didn't enter anything")

    cur.execute(query)
    output = cur.fetchall()
    print output
    raw_input(" ")
    cur.commit
main()