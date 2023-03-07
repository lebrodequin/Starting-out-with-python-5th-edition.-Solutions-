file_var = open('morse.txt', 'r')
symbol = []
morsesymbol = []

line = file_var.readline()
while line != '':
    line = line.rstrip('\n')
    symbol += line[0]
    morsesymbol.append(line[1:])
    line = file_var.readline()

file_var.close()

string = input('input string: ')
morse_string = []
for sym in string:
    position = symbol.index(sym.upper())
    morse_string.append(position)

for i in morse_string:
    print(f'{morsesymbol[i]} ', end='')
1