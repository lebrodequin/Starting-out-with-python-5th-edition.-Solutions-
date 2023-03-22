acc_list = []
filevar = open('charge_accounts.txt', 'r')
line = filevar.readline()
while line != '':
    line = int(line.rstrip('\n'))
    acc_list.append(line)
    line = filevar.readline()
print(acc_list)
filevar.close()

charge_acc = int(input('input charging account no: '))
if charge_acc in acc_list:
    print("it's here")
else:
    print("no it's not here")
