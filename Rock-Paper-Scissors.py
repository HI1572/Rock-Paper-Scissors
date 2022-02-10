'''
Lucio
January 10, 2022
This code will let you pay the game Rock-Paper-Scissors!
1. You will select Rock, Paper, or Scissors
2. The computer will then randomly select either Rock, Paper, or Scissors
3. Then the winner will be shown
'''

from random import randint #importing only randint function from random library
from time import sleep #importing only sleep function from time library

user_lost = 'You lost! Computer won!' #variable
user_won = 'You won! Computer lost!' #variable

def decide_winner(): # created a function
    u_score = 0
    c_score = 0
    
    while u_score < 3 and c_score < 3: #while loop lets you set parameters to run till they are met
        user_choice = input('Choose between R, P, or S ').upper()
        options = ['R', 'P', 'S']
        computer_choice = options[randint(0,2)]
        print('Computer selecting...')
        sleep(1)
        print('Computer chose ' + computer_choice)
        sleep(1)
        
        if user_choice == computer_choice: # if, elif, else statements to decide the winner
            print('You tied!')
        elif user_choice == 'R' and computer_choice == 'S':
            print(user_won)
            u_score = u_score + 1
        elif user_choice == 'P' and computer_choice == 'R':
            print(user_won)
            u_score = u_score + 1
        elif user_choice == 'S' and computer_choice == 'P':
            print(user_won)
            u_score = u_score + 1
        else:
            print(user_lost)
            c_score = c_score + 1
        
        print('User Score: ' + str(u_score) + ' - ' + 'Computer Score: ' + str(c_score)) #shows you what the score is
        
        if u_score == 3: #total game score win or lose
            print('GAME OVER. YOU WIN!')
        elif c_score == 3:
            print('GAME OVER. COMPUTER WINS!')
            
decide_winner() #called a function