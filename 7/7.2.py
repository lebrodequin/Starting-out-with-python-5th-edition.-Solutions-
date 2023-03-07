import random

def main():
    ranlist = []
    for i in range(7):
        ranlist.append(random.randint(1, 9))
    print(ranlist)

    for i in ranlist:
        print(i)

main()
