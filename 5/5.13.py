GRAVITY_CONST = 9.8

def main():
    for time in range(1, 11):
        dist = falling_distance(time)
        print(f'the distance is {dist:.1f} meters')

def falling_distance(sec):
    d = 0.5 * GRAVITY_CONST * sec ** 2
    return d


main()
