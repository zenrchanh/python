import random #importing modules, random for randint, time for sleep and os for file writing
import time
import os

print('Welcome to this guessing games')
time.sleep(2)
print('The game rules are very simple you be will asked to enter things like numbers and words.')
time.sleep(2)
print('Then a random word or number will be chosen as the winner and you must guess which one it is correctly.')
time.sleep(2)
print('You must go through 2 rounds and win both to successfully win.')
time.sleep(2)
print('Get ready in: ')

for a in range(3, -1, -1):
    print(a)
    time.sleep(1)
    
print('Let the games begin!')


print('Round One: Guess The Number , you will enter a valid number between 1-10 and see if it is the correct number, you have 3 tries good luck.')
 


def roundOne():
    rngNum = random.randint(1,10)
    print(rngNum)
    for guesses in range(0,3): # Up to 3 valid guesses
        while True:
            try:
                guessNums = int(input('Guess a number between 1-10: '))
                while guessNums <= 0 or guessNums > 10:
                    guessNums = int(input('Guess a number between 1-10: '))
            except ValueError:
                print('Please enter a valid number between 1-10.')
                continue
            else:
                break
        if guessNums == rngNum:
            print('You win, the number was: '+ str(rngNum))
        elif guessNums > rngNum:
            print('Too high sorry, try again.')
        elif guessNums < rngNum:
            print('Too low sorry, try again.')
        else:
            print('Out of guesses, you lose.')

roundOne()


print('Congratulations on winning the first game')