PEN = 0.01
NIK = 0.05
DIM = 0.10
QUA = 0.25

pen = int(input('input the number of pennies '))
nik = int(input('input the number of nickels '))
dim = int(input('input the number of dimes '))
qua = int(input('input the number of quaters '))

sum = pen * PEN + nik * NIK + dim * DIM + qua * QUA

if sum == 1:
    print('you win!')
elif sum < 1:
    print ('that is less than 1 dollar')
else:
    print ('that is more than 1 dollar')