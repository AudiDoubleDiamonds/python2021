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