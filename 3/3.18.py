veget = str(input('Is anyone in your party a vegetarian? '))
vegan = str(input('Is anyone in your party a vegan? '))
gluten = str(input('Is anyone in your party gluten-free? '))

if veget == 'yes':
    if vegan == 'yes':
        if gluten == 'yes':
            print (f'Here are your restaurant choices:\n'
                   f'\tThe Chef\'s Kitchen\n' 
                   f'\tCorner Cafe')
        else:
            print (f'Here are your restaurant choices:\n'
                   f'\tThe Chef\'s Kitchen\n' 
                   f'\tCorner Cafe')
    else:
        if gluten == 'yes':
            print (f'Here are your restaurant choices:\n'
                   f'\tMain Street Pizza Company\n'
                   f'\tThe Chef\'s Kitchen\n'
                   f'\tCorner Cafe')
        else:
            print (f'Here are your restaurant choices:\n'
                   f'\tMain Street Pizza Company\n'
                   f'\tThe Chef\'s Kitchen\n'
                   f'\tCorner Cafe\n'
                   f'\tMama\'s Fine Italian')
else:
    if vegan == 'yes':
        if gluten == 'yes':
            print (f'Here are your restaurant choices:\n'
                   f'\tThe Chef\'s Kitchen\n' 
                   f'\tCorner Cafe')
        else:
            print (f'Here are your restaurant choices:\n'
                   f'\tThe Chef\'s Kitchen\n' 
                   f'\tCorner Cafe')
    else:
        if gluten == 'yes':
            print (f'Here are your restaurant choices:\n'
                   f'\tMain Street Pizza Company\n'
                   f'\tThe Chef\'s Kitchen\n'
                   f'\tCorner Café')
        else:
            print (f'Here are your restaurant choices:\n'
                   f'\tJoe\'s Gourmet Burgers\n'
                   f'\tMain Street Pizza Company\n'
                   f'\tThe Chef\'s Kitchen\n'
                   f'\tCorner Cafe\n\n'
                   f'\tMama\'s Fine Italian')