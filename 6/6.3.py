def main():
    file_tmp = open('numbers.txt', 'r')
    numb = file_tmp.readline()
    count = 1
    while numb != '':
        numb = numb.rstrip('\n')
        print(f'{count}:\t{numb}')
        numb = file_tmp.readline()
        count += 1


main()
