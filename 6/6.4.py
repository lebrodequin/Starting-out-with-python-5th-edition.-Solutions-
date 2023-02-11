def main():
    file_tmp = open('names.txt', 'r')
    numb = file_tmp.readline()
    count = 0
    while numb != '':
        numb = file_tmp.readline()
        count += 1
    print(f'there are {count} names in the file')

main()
