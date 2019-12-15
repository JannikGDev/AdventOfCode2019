

def task5():

    data = read_input("input.txt")[0]

    code = [int(d) for d in data.split(',')]

    x = 5
    output = 0
    mode_a = 0
    mode_b = 0

    i = 0
    while True:
        if code[i] == 99 or i >= len(code):
            break

        i, code = perform_intruction(code, i, x)

    return code[0]


def perform_intruction(code, i, input_value):

    opcode = str(code[i])

    while len(opcode) < 5:
        opcode = '0' + opcode

    operation = int(opcode[3:])
    modes = [int(opcode[2]),int(opcode[1]),int(opcode[0])]

    def get_params(amount):
        params = []

        for j in range(amount):
            if modes[j] == 1:
                params.append(code[i+j+1])
            else:
                params.append(code[code[i + j + 1]])

        return params





    if operation == 1:
        params = get_params(3)
        code[code[i+3]] = params[1] + params[0]
        i += 4

    if operation == 2:
        params = get_params(3)
        code[code[i+3]] = params[1] * params[0]
        i += 4

    if operation == 3:
        params = get_params(1)
        code[code[i+1]] = input_value
        i += 2

    if operation == 4:
        params = get_params(1)
        print(params[0])
        i += 2

    # Jump if true
    if operation == 5:
        params = get_params(2)
        if params[0] != 0:
            i = params[1]
        else:
            i += 3

    # Jump if false
    if operation == 6:
        params = get_params(2)
        if params[0] == 0:
            i = params[1]
        else:
            i += 3

    # Less than
    if operation == 7:
        params = get_params(2)
        if params[0] < params[1]:
            code[code[i + 3]] = 1
        else:
            code[code[i + 3]] = 0

        i += 4

    # equals
    if operation == 8:
        params = get_params(2)
        if params[0] == params[1]:
            code[code[i + 3]] = 1
        else:
            code[code[i + 3]] = 0

        i += 4

    return i, code



def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task5()