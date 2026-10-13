"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game
"""

import random
import sys

JAPANESE_NUMBERS = {
    1: 'ICHI',
    2: 'NI',
    3: 'SAN',
    4: 'SHI',
    5: 'GO',
    6: 'ROKU'
}

# Brian Palm modification:
# Added information about the 10 mon bonus.
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

Bonus: If the dice total is 2 or 7, you receive a 10 mon bonus.
''')

purse = 5000

while True:  # Main game loop.

    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')

    while True:

        # Brian Palm modification:
        # Changed input prompt to BP:
        pot = input('BP: ')

        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        elif not pot.isdecimal():
            print('Please enter a number.')

        elif int(pot) > purse:
            print('You do not have enough to make that bet.')

        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:

        # Brian Palm modification:
        # Changed input prompt to BP:
        bet = input('BP: ').upper()

        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Brian Palm modification:
    # Added 10 mon bonus for rolls totaling 2 or 7.
    roll_total = dice1 + dice2

    if roll_total == 2 or roll_total == 7:
        print('The dice total was', roll_total)
        print('You received a 10 mon bonus!')
        purse = purse + 10

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0

    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    if playerWon:
        print('You won! You take', pot, 'mon.')

        purse = purse + pot

        # Brian Palm modification:
        # Changed house fee from 10% to 12%.
        house_fee = int(pot * 0.12)

        print('The house collects a', house_fee, 'mon fee.')

        purse = purse - house_fee

    else:
        purse = purse - pot
        print('You lost!')

    print('You now have', purse, 'mon.')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
