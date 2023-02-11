def main():
    score1 = int(input('input 1st score (1 to 100): '))
    score2 = int(input('input 2nd score (1 to 100): '))
    score3 = int(input('input 3rd score (1 to 100): '))
    score4 = int(input('input 4th score (1 to 100): '))
    score5 = int(input('input 5th score (1 to 100): '))

    avg = calc_average(score1, score2, score3, score4, score5)
    print(f'average score is {avg}')

    print(f'Score\tLetter Grade')
    for grade in [score1, score2, score3, score4, score5]:
        print (grade,'\t\t', end='')
        print(score_n_grade(grade))

def calc_average(num1, num2, num3, num4, num5):
    avg = (num1 + num2 + num3 + num4 + num5) / 5
    return avg

def score_n_grade(num):
        if num < 60:
            return ('f')
        elif 60 <= num <= 69:
            return ('d')
        elif 70 <= num <= 79:
            return ('c')
        elif 80 <= num <= 89:
            return ('b')
        elif 90 <= num <=100:
            return ('a')

main()

