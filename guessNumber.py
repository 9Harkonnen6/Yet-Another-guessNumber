from random import *

while True:
    try:
        numberRange = int(input('I should generate a number from 0 to...?' "\n" ))
        number = randrange(numberRange)
        a = int(input('Input number: '))

        if number == a:
            print(f'You guessed! Number you were looking for was {number}')
            number = randrange(10)
        elif number < a:
            print('Too big')
        else:
            print('Too small')
    except ValueError:
        print(f'You need to input number, silly')
        pass
    
    

