import pickle

test_averages = {'Janelle': 98,
                 'Sam': 87,
                 'Jennifer': 92,
                 'Thomas': 74,
                 'Sally': 89,
                 'Zeb': 84
                 }

out_file = open('mydata.dat', 'wb')
pickle.dump(test_averages, out_file)
out_file.close()