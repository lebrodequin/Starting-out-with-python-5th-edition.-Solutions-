day_num = int(input('input number between 1 and 7 '))
if day_num>7 or day_num<1:
    print('the number must be from 1 to 7, you stupid bastard')
else:
    if day_num==1:
        print('monday')
    elif day_num==2:
        print('tuesday')
    elif day_num==3:
        print('wednesday')
    elif day_num==4:
        print('thursday')
    elif day_num==5:
        print('friday')
    elif day_num==6:
        print('saturday')
    else:
        print('sunday')
