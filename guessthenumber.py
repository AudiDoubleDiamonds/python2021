# 2020.12.26
# guess the number

import random
det='y'
while det=='y':
    number=int(1000*random.random())+1
    print('I have a number between 1 and 1000.')
    print('Can you guess my number?')
    print('Please type your first guess.')
    guess=0
    counter=0
    while number!=guess:
        guess=input()#input后面是str形式
        guess=int(guess)
        counter=counter+1
        if number==guess:#判断用两个等号
            print('Excellent! You guessed the number!')
        elif number<guess:
            print('Too high. Try again.')
        else:
            print('Too low. Try again.')
    print('You have guessed',counter,'times.')
    if counter<10:
        print('Either you know the secret or you got lucky!')
    elif counter==10:
        print('Ahah! You know the secret!')
    elif counter>10:
        print('You should be able to do better!')
    det=input('Would you like to play again? (y or n) ')

