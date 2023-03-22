import pickle
load_file = open('mydata.dat', 'rb')
var = pickle.load(load_file)
print(f'{type(var)}, {var}')
load_file.close()