#2020.1.24
#信用卡验证

#Read the credit card number
error=True
while error==True:#输错数字重试
    number=input('Please enter the credit card number: ')
    try:
        num_int=int(number)
        if num_int<10 or num_int>99999999:
            error=True
            print('Invalid input. 2-8 digits please. ')
        else:
            error=False
    except:
        print('Invalid input. ')
        error=True
        
#Stage one
length=len(number)
if length==2:
    num_alt=number[1]+number[0]
elif length==3:
    num_alt=number[2]+number[1]+number[0]
else:
    counter=0
    num_alt=''
    while counter<length:
        num_alt=num_alt+str(int(number[counter])*3%10)
        counter=counter+1
print('Encoded number is:',num_alt)

#Stage two
if length==8:
    choice=input('Do you want to enable the extra protection? (y or n)')
    if choice=='y':
        counter2=0
        num_ex=''
        while counter2<8:
            num_ex=num_alt[counter2]+num_ex
            counter2=counter2+1
        print('Encoded number is:',num_ex)

#stage three
num_decode=''
choice2=input('Do you want to know the decode? (y or n)')
if choice2=='y' and length==8:    
    counter3=7
    while counter3>=0:
        num_decode=num_ex[counter3]+num_decode
        counter3=counter3-1
    counter3=7
    print(num_decode)
    num_decode2=''
    while counter3>=0:
        if num_decode[counter3]==0:
            num_decode[counter3]=0
        elif num_decode[counter3]==1:
            num_decode[counter3]=7
        elif num_decode[counter3]==2:
            num_decode[counter3]=4
        elif num_decode[counter3]==3:
            num_decode[counter3]=1
        elif num_decode[counter3]==4:
            num_decode[counter3]=8
        elif num_decode[counter3]==5:
            num_decode[counter3]=5
        elif num_decode[counter3]==6:
            num_decode[counter3]=2
        elif num_decode[counter3]==7:
            num_decode[counter3]=9
        elif num_decode[counter3]==8:
            num_decode[counter3]=6
        else:
            if num_decode[counter3]==9:
                num_decode[counter3]=3
        counter3=counter3-1
        num_decode2=num_decode[counter3]+num_decode2
    print('The decoded number is',num_decode2)
elif choice2=='y' and length>=4 and length<8:
    counter4=length
    counter4=counter4-1
    while counter4>=0:
        if num_decode[counter4]==0:
            num_decode[counter4]=0
        elif num_decode[counter4]==1:
            num_decode[counter4]=7
        elif num_decode[counter4]==2:
            num_decode[counter4]=4
        elif num_decode[counter4]==3:
            num_decode[counter4]=1
        elif num_decode[counter4]==4:
            num_decode[counter4]=8
        elif num_decode[counter4]==5:
            num_decode[counter4]=5
        elif num_decode[counter4]==6:
            num_decode[counter4]=2
        elif num_decode[counter4]==7:
            num_decode[counter4]=9
        elif num_decode[counter4]==8:
            num_decode[counter4]=6
        else:
            if num_decode[counter4]==9:
                num_decode[counter4]=3
        counter4=counter4-1
    print('The decoded number is',num_decode)
elif choice2=='y' and length==3:
    num_decode=num_alt[2]+num_alt[1]+num_alt[0]
    print('The decoded number is',num_decode)
else:
    num_decode=num_alt[1]+num_alt[0]
    print('The decoded number is',num_decode)
