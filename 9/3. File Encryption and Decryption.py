codes = {'a': 't', 'b': '(', 'c': 'u',
         'd': '3', 'e': '2', 'f': '[',
         'g': '0', 'h': '=', 'i': '@',
         'j': '5', 'k': '%', 'l': '*',
         'm': '&', 'n': 'o', 'o': '+',
         'p': 'q', 'q': '8', 'r': '4',
         's': '6', 't': '.', 'u': ';',
         'v': '1', 'w': '!', 'x': '7',
         'y': 'T', 'z': 'M', ' ': '^',
         '.': 'j', ',': 'P', '!': '$',
         '?': '#', '-': 'E', '0': 'z',
         '1': 'Y', '2': 'G', '3': '@',
         '4': 'H', '5': 'A', '6': 'L',
         '7': 'W', '8': 'i', '9': 'C',
         }

# encryption of the file
file_var = open('text.txt', 'r')
encrypted_file = open('encrypted.txt', 'w')

line = file_var.readline()
while line != '':
    line = line.rstrip('\n')
    encrypted_line = ''
    for i in range(len(line)):
        encrypted_line += str(codes.get(line[i]))
    encrypted_file.write(encrypted_line + '\n')
    line = file_var.readline()

file_var.close()
encrypted_file.close()

# decryption of file
codes_key_list = list(codes.keys())
codes_val_list = list(codes.values())

file_var = open('encrypted.txt', 'r')
decrypted_file = open('decrypted.txt', 'w')
line = file_var.readline()
while line != '':
    line = line.rstrip('\n')
    decrypted_line = ''
    for i in range(len(line)):
        pos = codes_val_list.index(line[i])
        decrypted_line += codes_key_list[pos]
    decrypted_file.write(decrypted_line + '\n')
    line = file_var.readline()
