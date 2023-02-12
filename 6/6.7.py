import random

def main():
    tempfile = open('random_numbers.txt', 'w')
    quan = int(input('how many numbers? '))
    for i in range(quan):
        tempfile.write(str(random.randint(1, 500)) + '\n')
    tempfile.close


main()
