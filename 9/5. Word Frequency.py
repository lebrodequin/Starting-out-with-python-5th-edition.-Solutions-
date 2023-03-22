file_var = open('text.txt', 'r')

line = file_var.readline()
word_list = []
while line != '':
    line.rstrip('\n')
    line_list = line.split()
    for i in range(len(line_list)):
        word_list.append(line_list[i])
    line = file_var.readline()

count = 0
freq_dict = {}
for i in range(len(word_list)):
    for j in range(len(word_list)):
        if word_list[i] == word_list[j]:
            count += 1
    freq_dict[word_list[i]] = count
    count = 0

file_var.close()

print(freq_dict)