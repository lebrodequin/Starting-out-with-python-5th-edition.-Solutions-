def main():
    file_var = open('students.txt', 'r')
    name = file_var.readline()
    while name != '':
        score = file_var.readline()
        name = name.rstrip('\n')
        score = score.rstrip('\n')

        print(name)
        print(score)

        name = file_var.readline()
    file_var.close()


main()