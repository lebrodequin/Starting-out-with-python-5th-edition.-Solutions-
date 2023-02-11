pocket_num = int(input('input pocket number\n'))

if pocket_num ==0:
    print ('green')
elif 1 <= pocket_num <= 10 and pocket_num % 2 != 0:
    print ('red')
elif 1 <= pocket_num <= 10 and pocket_num % 2 == 0:
    print ('black')
elif 11 <= pocket_num <= 18 and pocket_num % 2 != 0:
    print ('black')
elif 11 <= pocket_num <= 18 and pocket_num % 2 == 0:
    print ('red')
elif 19 <= pocket_num <= 28 and pocket_num % 2 != 0:
    print ('red')
elif 19 <= pocket_num <= 28 and pocket_num % 2 == 0:
    print ('black')
elif 28 <= pocket_num <= 36 and pocket_num % 2 != 0:
    print ('black')
elif 28 <= pocket_num <= 36 and pocket_num % 2 == 0:
    print ('red')