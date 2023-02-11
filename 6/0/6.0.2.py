def main():
    file_var = open('myname.txt', 'r')
    print(file_var.readline())
    file_var.close()


main()