length1 = float(input('input length of the 1st rectangle '))
width1 = float(input('input width of the 1st rectangle '))
length2 = float(input('input length of the 2nd rectangle '))
width2 = float(input('input width of the 2nd rectangle '))

sq1 = length1 * width1
sq2 = length2 * width2

if sq1 > sq2:
    print('the 1st rectangle has a bigger square than the 2nd one')
elif sq1 > sq2:
    print('the 2nd rectangle has a bigger square than the 1st one')
else:
    print('rectangles have the same square')
