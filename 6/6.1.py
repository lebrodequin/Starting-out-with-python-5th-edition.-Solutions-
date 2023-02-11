def main():
    file_tmp = open('numbers.txt', 'r')
    numb = file_tmp.readline()
    while numb != '':
        numb = numb.rstrip('\n')
        print(numb)
        numb = file_tmp.readline()


main()
