def main():
    filename1 = 'decrypted.txt'
    filemane2 = 'text.txt'

    set_filename1, set_filename2 = set(file_2_list(filename1)), set(file_2_list(filemane2))
    set_intersection = set_filename1.intersection(set_filename2)
    set_difference = set_filename1.difference(set_filename2)
    set_difference_reverse = set_filename2.difference(set_filename1)
    set_symmetric_difference = set_filename1.symmetric_difference(set_filename2)

    print(f'here is a list of unique words in first file: {set_filename1}\n'
          f'here is a list of unique words in second file: {set_filename2}\n'
          f'here is list of the words that appear in both files: {set_intersection}\n'
          f'here is a list of the words that appear in the first file but not the second: {set_difference}\n'
          f'here is a list of the words that appear in the second file but not the first {set_difference_reverse}\n'
          f'here is a ist of the words that appear in either the first or second file, but not both: {set_symmetric_difference}')

def file_2_list(filename):
    file_var = open(filename, 'r')
    line = file_var.readline()
    word_list = []
    while line != '':
        line.rstrip('\n')
        line_list = line.split()
        for i in range(len(line_list)):
            word_list.append(line_list[i])
        line = file_var.readline()
    return word_list


main()
