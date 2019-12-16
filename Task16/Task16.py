import numpy as np
import math

def task16_1():

    data = read_input("input.txt")[0]

    sequence = np.array([int(digit) for digit in data])
    pattern = np.array([0, 1, 0, -1])

    for phase in range(100):
        sequence = apply_phase(sequence, pattern)

    print(sequence)

def task16_2():
    data = read_input("input.txt")[0]

    sequence = np.array([int(digit) for digit in data])

    offset = sequence[:4]
    offset = int("".join([str(digit) for digit in offset]))

    final_output = sequence[offset:offset + 8]

    return


def apply_phase(input, pattern):

    output = []
    pattern_i = pattern.copy()

    for i in range(len(input)):
        pattern_i = np.repeat(pattern, (i + 1))
        pattern_i = np.tile(pattern_i, math.ceil((len(input)+1) / len(pattern * (i + 1))))
        result = np.dot(input, pattern_i[1:len(input)+1])

        result = abs(result) % 10
        output.append(result)

    return np.array(output)

def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task16_1()
