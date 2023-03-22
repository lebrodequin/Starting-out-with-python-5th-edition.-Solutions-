def main():
    file_var = open('text.txt', 'r')
    line = file_var.readline()
    sentece = []
    while line != '':
        sentece.append(line.split())
        line = file_var.readline()

    num_of_words = 0
    for i in range(len(sentece)):
        for j in sentece[i]:
            num_of_words += 1
    print(f'average number of words is {num_of_words/len(sentece)}')

main()
