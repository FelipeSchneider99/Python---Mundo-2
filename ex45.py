# crie um programa que faça o computador jogar jokenpo com voce
from random import randint
from time import sleep

jokenpo = ('Rock', 'Paper', 'Scissors')
comp = randint(0, 2)
print('JOKENPO')
print('-=' * 12)
print('[0] ROCK'
      '\n[1] PAPER'
      '\n[2] SCISSORS')
print('-=' * 12)
user = int(input('What is your choice: '))
print('')
print('Rock')
sleep(0.5)
print('Paper')
sleep(0.5)
print('Scissors')
sleep(1)
print('SHOOT!!')
print('')
print('-=' * 12)
if user == 0: #ROCK
    if comp == 0: #ROCK
        print('Tie')
    elif comp == 1: #PAPER
        print('You lose...')
    elif comp == 2: #SCISSORS
        print('You win!!')

elif user == 1: #PAPER
    if comp == 0: #ROCK
        print('You win...')
    elif comp == 1: #PAPER
        print('Tie')
    elif comp == 2: #SCISSORS
        print('You lose...')

elif user == 2: #SCISSORS
    if comp == 0: #ROCK
        print('You lose...')
    elif comp == 1: #PAPER
        print('You win!!')
    elif comp == 2: #SCISSORS
        print('Tie')

else:
    print('Invalid choice. You lose!')

print('-=' * 12)
print('')
print(f'User: {jokenpo[user]}'
      f'\nComputer: {jokenpo[comp]}')
print('')
print('-=' * 12)
