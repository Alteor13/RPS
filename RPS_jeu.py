"""Jeu de Pierre-Papier-Ciseau"""

import random
import os
import re
import sys

def check_play_status():
    """Vérifie qu'un joueur désire jouer à l'aide des réponses yes et no"""

    valid_responses = ['yes', 'no']
    while True:
        try:
            response = input('Do you wish to play again? (Yes or No): ')
            if response.lower() not in valid_responses:
                raise ValueError('Yes or No only')

            if response.lower() == 'yes':
                return True
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Thanks for playing!')
            sys.exit()

        except ValueError as err:
            print(err)

def play_rps():
    """Joue un match de Pierre-Papier-Ciseaux entre deux joueurs"""
    play = True
    while play:
        print('')
        print('Rock, Paper, Scissors - Shoot!')

        user_choice = input('Choose your weapon'
                           ' [R]ock], [P]aper, or [S]cissors: ')

        if not re.match("[SsRrPp]", user_choice):
            print('Please choose a letter:')
            print('[R]ock, [P]aper, or [S]cissors')
            continue

        print(f'You chose: {user_choice}')

        choices = ['R', 'P', 'S']
        opp_choice = random.choice(choices)

        print(f'I chose: {opp_choice}')

        if opp_choice == user_choice.upper():
            print('Tie!')
            play = check_play_status()
        elif opp_choice == 'R' and user_choice.upper() == 'S':
            print('Rock beats scissors, I win!')
            play = check_play_status()
        elif opp_choice == 'S' and user_choice.upper() == 'P':
            print('Scissors beats paper! I win!')
            play = check_play_status()
        elif opp_choice == 'P' and user_choice.upper() == 'R':
            print('Paper beats rock, I win!')
            play = check_play_status()
        else:
            print('You win!\n')
            play = check_play_status()

if __name__ == '__main__':
    play_rps()
