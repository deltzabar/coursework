#NB: x has been used throughout as a temporary variable. It is unimportant!

#####IMPORTS#####

from time import *
from random import *
import sqlite3 as lite #used for SQL

#####SUB-PROGRAMS#####

###login###

def login(): #making a function, paremeter is the player's name
    playername = ()
    Authorised_Users = ['sofia','devante','salmonella','alaska','amandla','emily','cecilia','cecile','jose','npedro','cecil','kitchen','castanette','brigitte'] #array of all authorised user's names
    accepted = False #flag for loop -> used to stop when there has been an authorised player name entered
    while not accepted: #condition controlled loop
        correct = False #flag for loop -> used to stop when correct format entered
        while not correct: #condition controlled loop
            playername = input('''\nPlease enter a player's name: ''').lower() #asks players to input name, sanitisation
            if playername.isalpha(): #checks if the name entered is all letters with no spaces
                correct = True #ends inner loop -> correct format
                check = len(Authorised_Users)-1 #finds out length of input
                while check > -1: #count controlled looop, loops the length of the word
                    if playername == Authorised_Users[check]: #checks that the input matches an authorised user's name
                        print('Accepted') #########################################################################################
                        accepted = True #ends outer loop -> does match
                    check -= 1 #increments loop
                if not accepted: #checks if the name has been accepted
                    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    sleep(0.2)
                    print('!                                                !')
                    sleep(0.2)
                    print('!         You are not an authorised player       !') #outputs a message
                    sleep(0.2)
                    print('!                                                !')
                    sleep(0.2)
                    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                    sleep(1)
                    print('\nPlease enter a valid name!')
            else: #checks if the input is the wrong format
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                sleep(0.2)
                print('!                                                !')
                sleep(0.2)
                print('!     Please ensure you enter only letters       !') #outputs a message
                sleep(0.2)
                print('!                                                !')
                sleep(0.2)
                print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                sleep(1)
    return playername #returns player's name

###dice###

def dice(die): #parameter is the result of the randomised die roll in code
    if die == 1: #Using selection to decide which image should be displayed
        print(' _____') #ASCII art image of a die
        print('|     |')
        print('|     |')
        print('|  O  |')
        print('|     |')
        print('|_____|\n')
    elif die == 2:
        print(' _____')
        print('|     |')
        print('| O   |')
        print('|     |')
        print('|   O |')
        print('|_____|\n')
    elif die == 3:
        print(' _____')
        print('|     |')
        print('|O    |')
        print('|  O  |')
        print('|    O|')
        print('|_____|\n')
    elif die == 4:
        print(' _____')
        print('|     |')
        print('| O  O|')
        print('|     |')
        print('|O  O |')
        print('|_____|\n')
    elif die == 5:
        print(' _____')
        print('|     |')
        print('|O   O|')
        print('|  O  |')
        print('|O   O|')
        print('|_____|\n')
    else:
        print(' _____')
        print('|     |')
        print('| O O |')
        print('| O O |')
        print('| O O |')
        print('|_____|\n')

###dice roll###

def dice_roll(pointsscored, bonuspoints): #making a function, parameters are the numbers of points scored in the game and the bonus points
    die1 = randint(1,6) #chooses a random number from 1-6 for die 1
    die2 = randint(1,6) #and die 2 

    x = input('Press enter to roll your first die') #input means they must press enter for the next line
    dice(die1)
    sleep(1)
    x = input('Press enter to roll your second die') #same again
    dice(die2)
    sleep(1)
    pointsscored = die1 + die2 #adding the dice together for the points scored that round
    print('''That's '''+str(pointsscored)+' points in total')
    sleep(2)
    isiteven = pointsscored%2 #pointsscored MOD 2 to check if it is even
    if isiteven == 0: #checking if it is even, if it equals 0, it is
        bonuspoints += 10 #add 10 to bonus points for an even number
        print('Because that is even, you score a bonus 10 points!')
        sleep(2)
        print('''That's '''+ str(pointsscored+bonuspoints)+' points in total!') #outputs total number of points accumulated so far
        sleep(1)
        if die1 == die2: #if they are the same then
            extraroll = randint(1,6) #the equivalent of rolling another die
            bonuspoints += extraroll
            print('Because you rolled a double, you get to roll again!')
            sleep(1)
            x = input('Press enter to roll the die!')
            dice(extraroll)
            sleep(1)
            print('That makes '+str(bonuspoints+pointsscored)+' points in total!')
            
    else:
        bonuspoints -= 5 #if it is not even, takeaway 5 from the score
        print('Because that is odd, you lose 5 points!')
        sleep(1)
        print('That means that you have got '+(str(pointsscored+bonuspoints))+' points this round!')
    return pointsscored, bonuspoints #return how many points scored that round and the bonus points scored
    


###tie breaker###

def tie_breaker(player1name, player2name): #uses parameters of player names so that the name of the winner can be returned
    print("**************************************************") 
    sleep(0.2)
    print("*                                                *")
    sleep(0.2)
    print("*                                                *")
    sleep(0.2)
    print('*            Welcome to the tie breaker!         *')
    sleep(0.2)
    print("*                                                *")
    sleep(0.2)
    print('''*              You've scored the same,           *''')
    sleep(0.2)
    print('*              so must each roll a die           *')
    sleep(0.2)
    print('*              until a winner is found!          *')
    sleep(0.2)
    print("*                                                *")
    sleep(0.2)
    print("*                                                *")
    sleep(0.2)
    print("**************************************************")

    equal = True #flag, used to stop code when dice are not equal
    while equal: #condition controlled loop, continues looping until a winner is decided
        player1die = randint(1,6) #effectively rolls a die for each player
        player2die = randint(1,6)
        sleep(2)
        x = input(player1name+' , press enter to roll your die!')
        dice(player1die)
        sleep(1)
        x = input(player2name+' , press enter to roll your die!')
        dice(player2die)
        sleep(1)
        if player1die == player2die: #checks if they are the same
            print("**************************************************")
            sleep(0.2)
            print('*                                                *')
            sleep(0.2)
            print('''*             You've rolled the same!            *''')
            sleep(0.2)
            print('*                                                *')
            sleep(0.2)
            print('*              So you need to roll again         *')
            sleep(0.2)
            print('*                                                *')
            sleep(0.2)
            print("**************************************************")
        else: #checks if they are not the same
            equal = False #if so changes the flag so that dice do not continue to be rolled 
            if player1die > player2die: #checks with die has a higher value -> not >= as cannot be equal (see above)
                print("**************************************************")
                sleep(0.2)
                print()
                print('                 '+player1name+ ' wins!')
                print()
                sleep(0.2)
                print("**************************************************")
                winner = player1name 
            else:
                print("**************************************************")
                sleep(0.2)
                print()
                print('                 '+player2name+ ' wins!')
                print()
                sleep(0.2)
                print("**************************************************")
                winner = player2name
    return winner #so that this can be used in the end game

###a turn###

def a_turn(playerpoints,playerbonus,playerscore): #parameters are passed in to be used in the dice roll and so that the results of that can be added to it
    points,bonus = dice_roll(playerpoints,playerbonus) #different varaible names must be used so that confusion does not ensue from the original value passed in and the current value
    totalscore = playerscore + points + bonus #adding up the total score
    if totalscore < 0: #to make sure that the total score never dips below 0, if the score is below 0 it is merely set to 0
        totalscore = 0
    print('your score is '+str(totalscore)+' points in total!')
    return totalscore #returns the total score to be used as player1score or player2score

###end game (using textfiles)###

def end_game(winner, winnerscore):
    print('\nTHE WINNER OF THIS ROUND IS ' + winner.upper() + ' WITH ' + str(winnerscore) + ' POINTS!\n')
    print('How do you compare against the top 5 winners?\n')
    toprint = (winner + ' ' + str(winnerscore))
    file = open("scores.txt","a")  #########ADD COMMENTS###########
    file.write(toprint+'\n')
    file.close()
    file = open("scores.txt","r")
##    for i in range (1,6):
##        x = file.readline()
##        if not x:
##            break
##        print(x)
##    while True:
##        line = file.readline()
##        if not line:
##            break
##        print(line)
##        sleep(0.1)
##    file.close()

    #ADDING WINNER TO DATABASE USING SQL
    con = lite.connect("scores.db") 
    cur = con.cursor()
    cur.execute('''INSERT into scores(Name, Score) VALUES(?,?)''', (winner, winnerscore))
    con.commit()
    #GETTING THE TOP FIVE SCORES
    s = '''SELECT * FROM scores ORDER BY Score DESC LIMIT 5;'''
    cur.execute(s)
    sortedscores = cur.fetchall()
    con.close()
    for item in sortedscores:
        print(item)

#####MAIN GAME#####

###intro###

def intro():
    print("**************************************************") #UI
    sleep(0.2)
    print("*                                                *")
    sleep(0.2)
    print("*                                                *")
    sleep(0.2)
    print("*         WELCOME TO THE DICENATOR 500           *")
    sleep(0.2)
    print("*                                                *")
    sleep(0.2)
    print("*         Do you know how to play? (y/n)         *")
    sleep(0.2)
    print("*                                                *")
    sleep(0.2)
    print("*                                                *")
    sleep(0.2)
    print("**************************************************")
    x = input().lower()
    if x == 'y':
        print('''let's get started then!''')
    elif x != 'y':
        print("**************************************************")
        sleep(0.2)
        print("*                                                *")
        sleep(0.2)
        print("*        Each player will roll two dice          *")
        sleep(0.2)
        print("*          Depending on what you roll            *")
        sleep(0.2)
        print("*          you might get bonus points!           *")
        sleep(0.2)
        print("*    After 5 rounds, the highest score wins!     *")
        sleep(0.2)
        print("*                                                *")
        sleep(0.2)
        print("**************************************************\n")
    player1name = login() #runs login with the parameter of player1name, returns to that variable
    print('''now it's player 2''') #so that the players know it is now the other person's turn to input their name
    player2name = login() #runs login with player2name as the parameter
    return player1name, player2name

###game###

def game(player1name,player2name): #defining the function game, which is one run through of the game with 5 turns each
    player1score = 0 #defines the variables used for the player's scores
    player2score = 0
    sleep(1)
    for i in range (0,5): #count controlled loop to make sure that each player has five turns
        sleep(1)
        print('\n**************************************************')
        sleep(0.2)
        print('*                                                *')
        sleep(0.2)
        print('*                                                *')
        sleep(0.2)
        print('*             Welcome to round ' + str(i+1) + '!                *')
        sleep(0.2)
        print('*                                                *')
        sleep(0.2)
        print('*                                                *')
        sleep(0.2)
        print('**************************************************')
        player1points = 0 #defines the player points and bonuses within the loop in order that they be set to 0 at the beginning of every go
        player1bonus = 0
        sleep(1)
        print('\n**************************************************')
        sleep(0.2)
        print('''              It's '''+ player1name+''''s turn ''') #outputs whose turn it is so the players can keep track
        sleep(0.2)
        print('\n**************************************************')
        player1score = a_turn(player1points,player1bonus,player1score) #calls the function a_turn, returns result to variable player1score
        player2points = 0 #the same as above, but for the second player
        player2bonus = 0
        print()
        sleep(1)
        print('\n**************************************************')
        sleep(0.2)
        print('''              It's '''+ player2name+''''s turn ''') #outputs whose turn it is so the players can keep track
        sleep(0.2)
        print('\n**************************************************')
        player2score = a_turn(player2points,player2bonus,player2score)
                                                               ##after the 5 rounds have been played, this section decides what will happen next
    if player1score == player2score: #if both players have the same score, there is a tiebreaker to find the winner
        winner = tiebreaker(player1name,player2name) #returns the name of the winner from the function tie_breaker
    elif player1score > player2score: #checks if player1score is larger than player2score
        winner = player1name #if so, player1 is the winner
    else:
        winner = player2name
    if winner == player1name:
        end_game(winner,player1score)
    else:
        end_game(winner,player2score)
        
###main game###

def main_game(): #defining the function 'main_game' which brings all of the functions together
    player1name,player2name = intro() #runs intro, which runs login twice and ouputs some messages
    keepgoing = True #the flag 'keepgoing' will be used to break the loop when the playersno longer wish to continue playing
    while keepgoing: #uses a condition controlled loop, controlled by the flag 'keep going'
        game(player1name, player2name) #runs the function 'game' which uses the function a turn as well as calling the function endgame etc.
        yorn = False #the flag 'yorn' will be used to break the loop when the user answers with either y or n
        while not yorn: #a condition controlled loop controlled by the flag 'yorn'
            x = input('\nWOULD YOU LIKE TO PLAY AGAIN? (Y/N): ').lower() #asks the user to answer whether they would like to continue playing, the .lower() sanitises the answer
            if x == 'y' or x == 'n': #checks if the user has answered y OR n
                yorn = True #if so, makes yorn TRUE, which will break the inner loop
            else: 
                print('That is not a valid answer') #if not, outputs an appropriate message and does not change the flag so the loop continues
                sleep(1)
                print('Please answer with "y" or "n"')
        if x == 'y': #checks if the user has answered 'y' to the question
            print('''\nok we'll start the game again with the same players''') #outputs a suitable message, using \n to make the message standout
        else:
            print('Good Bye!') 
            sleep(2)
            keepgoing = False #changes flag to break outer loop, game ends
    


######THE RUN######

main_game()








        
