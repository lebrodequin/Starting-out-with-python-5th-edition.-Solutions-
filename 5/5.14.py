def main():
    mass = float(input('input mass, kg: '))
    velocity = float(input('input velocity, mps: '))
    ke = kinetic_energy(mass, velocity)
    print(f'kinetic energy is {ke}')


def kinetic_energy(mas, vel):
    ke = 0.5 * mas * vel ** 2
    return ke

main()