def main():
    file_var = open('numberlist.txt', 'r')
    for i in range(100):
        print(f'{file_var.readline()}')
    file_var.close()


main()