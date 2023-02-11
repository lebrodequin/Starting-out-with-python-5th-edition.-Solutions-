MILES_IN_KM = 0.6214

def main():
    kilom = float(input('how many km? '))
    mil = km_to_miles(kilom)
    print(mil)

def km_to_miles(km):
    ml = km * MILES_IN_KM
    return ml

main()
