#2021.1.8
#骰子赌博
import random

bankBalance=100
print('You have $',bankBalance,'in the bank.')
again='y'

while again=='y' and bankBalance>0:
    wager=0
    while wager>bankBalance or wager<=0:
        wager=input('Place your wager: ')#input后面是str形式
        wager=int(wager)
    win=True
    # Roll the dice and calculate the sum
    die1=int(6*random.random())+1#一共有几个数，random就乘几
    die2=int(6*random.random())+1
    number=die1+die2
    print('Player rolled',die1,'+',die2,'=',number)
    print('point is',number)
    if number==7 or number==11:
        win=True
    elif number==2 or number==3 or number==12:
        win=False
    else:
        point=number
        number=0
        while number!=7 and number!=point:
            number=int(6*random.random())+1
            number=number+int(6*random.random())+1
            print('number =',number)
            if number==point:
                win=True
            elif number==7:
                win=False
    if win==True:
        print('You win!')
        bankBalance=bankBalance+wager
    else:
        print('You lose.')
        bankBalance=bankBalance-wager
    print('Your new bankBalance is',bankBalance)
    if bankBalance>0:
        again=input('Would you like to try your luck again? (y or n) ')
if bankBalance==0:
    print('Game over. You busted!')
else:    
    print('Game ended. Your final balance is',bankBalance)