def main():
    fat = float(input('how many grams of fat? '))
    carb = float(input('how many grams of carbohydrate? '))
    fc = fat_calories(fat)
    cc = carb_calories(carb)
    print(f'you got {fc} calories from fat, and {cc} calories from carbohydrates')


def fat_calories(x):
    return x * 9


def carb_calories(x):
    return x * 4


main()
