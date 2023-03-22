import pickle

def main():
    file_var = open('dict.dat', 'rb')
    dictionary = pickle.load(file_var)
    keep_going = True
    while keep_going:
        selector = int(input(f'1 - Add\n'
                             f'2 - Edit\n'
                             f'3 - Delete\n'
                             f'4 - Print dict\n'
                             f'5 - Exit\n'))
        if selector == 1:
            add_kv(dictionary)
        elif selector == 2:
            edit_v_by_k(dictionary)
        elif selector == 3:
            delete_kv(dictionary)
        elif selector == 4:
            print(dictionary)
        elif selector == 5:
            keep_going = False
            out_file = open('dict.dat', 'wb')
            pickle.dump(dictionary, out_file)
            out_file.close()

    file_var.close()




def add_kv(dic):
    k = input('input name:\t')
    v = input('input e-mail:\t')
    dic[k] = v
    return dic

def edit_v_by_k(dic):
    k = input('input name you would like to change email:\t')
    v = input('input new email:\t\t\t\t\t')
    dic[k] = v
    return dic

def delete_kv(dic):
    k = input(f'input name you would like to delete: ')
    dic.pop(k)
    return dic


main()
