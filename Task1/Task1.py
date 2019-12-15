import numpy as np


def start():

    input_data = []

    with open("Input.txt") as file:
        for line in file:
            input_data.append(int(line.strip()))

    numbers = [calculate_module_fuel(module_mass) for module_mass in input_data]

    result = int(np.array(numbers).sum())

    print("Result: ")
    print(result)


def calculate_module_fuel(module_mass):
    total_fuel = calculate_fuel(module_mass)

    new_fuel = calculate_fuel(total_fuel)
    while new_fuel > 0:
        total_fuel += new_fuel
        new_fuel = calculate_fuel(new_fuel)

    return total_fuel

def calculate_fuel(mass):

    return max(0, (mass // 3) - 2)


if __name__ == "__main__":
    start()
