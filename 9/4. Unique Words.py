file_var = open('text.txt', 'r')

line = file_var.readline()
word_list = []
while line != '':
    line.rstrip('\n')
    line_list = line.split()
    for i in range(len(line_list)):
        word_list.append(line_list[i])
    line = file_var.readline()

file_var.close()

my_set = set(word_list)
print(my_set)