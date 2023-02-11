def main():
    filename = input('input file name: ')
    file_tmp = open(filename, 'r')
    numb = file_tmp.readline()
    for i in range(5):
        numb = numb.rstrip('\n')
        print(numb)
        numb = file_tmp.readline()


main()
