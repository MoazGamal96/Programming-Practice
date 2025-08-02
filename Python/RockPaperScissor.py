
import os
import random
import re
from logging.config import valid_ident


def check_play_status():
    valid_responses =['yes', 'no']
    while True:
        try:
            response =input('Do you wish to play again? (YES or no):')
            if response.lower() not in valid_responses:
                raise ValueError('yes or no')
            if response.lower () ==  'yes':
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear') 
                print('Thanks for Playing!')
                exit()
        except ValueError as err:
            print(err)
def play_rps():
    play = True
    while play:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print ('')
        print('Rock, Paper, Scissors - Shoot!')

        user_choice = input ('Choose your weaponnnn''[R]ock, [P]apr, [S]ceissors: ')
        if not re.match("[SsRrPp]", user_choice):
            print('Please choose a letter:')
            print('[R]ok, [P]aper, [S]cissors')
            continue
        print(f'You Chose: {user_choice}')
        choices =['R', 'P', 'S']
        opp_choice = random.choice(choices)

        print(f'I chose: {opp_choice}')
        if opp_choice == user_choice.upper():
            print('Tie')
            play = check_play_status ()
        elif opp_choice == 'R' and user_choice.upper () == 'S':
            print('Rock beats Scissors, I Win!')
            play =check_play_status()
        elif opp_choice == 'S' and user_choice.upper () == 'P':
            print('Scissors beats Paper, I Win!')
            play =check_play_status()
        elif opp_choice == 'P' and user_choice.upper () == 'R':
            print('Paper beats Rock, I Win!')
            play =check_play_status()
        else:
            print('You in!\n')
            play = check_play_status   
if __name__ == '__main__':
    play_rps()               