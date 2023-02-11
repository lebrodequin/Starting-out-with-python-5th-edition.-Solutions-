def main():
    found = False
    search = 'John Perz'
    temp_file = open('students.txt', 'r')
    new_file = open('temp.txt', 'w')
    line = temp_file.readline()
    while line != '':
        if search in line:
            print('ok')
        else:
            print('not ok')
        line = temp_file.readline()
    temp_file.close()


main()
