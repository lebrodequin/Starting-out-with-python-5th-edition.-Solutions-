def main():
    file_var = open('numberlist.txt', 'w')
    x = 0
    for i in range(100):
        x += 1
        file_var.write(f'{str(x)}\n')
    file_var.close()


main()