
def task7_1():

    phases = [0,1,2,3,4]

    max = 0

    for i1 in range(5):
        for i2 in range(4):
            for i3 in range(3):
                for i4 in range(2):
                    phase_setting = []
                    used_phases = phases.copy()
                    phase_setting.append(used_phases.pop(i1))
                    phase_setting.append(used_phases.pop(i2))
                    phase_setting.append(used_phases.pop(i3))
                    phase_setting.append(used_phases.pop(i4))
                    phase_setting.append(used_phases[0])

                    value = get_thruster_signal(phase_setting)
                    if value > max:
                        max = value

    print(max)


def task7_2():

    phases = [5, 6, 7, 8, 9]

    max = 0

    for i1 in range(5):
        for i2 in range(4):
            for i3 in range(3):
                for i4 in range(2):
                    phase_setting = []
                    used_phases = phases.copy()
                    phase_setting.append(used_phases.pop(i1))
                    phase_setting.append(used_phases.pop(i2))
                    phase_setting.append(used_phases.pop(i3))
                    phase_setting.append(used_phases.pop(i4))
                    phase_setting.append(used_phases[0])

                    value = run_loop(phase_setting)
                    if value > max:
                        max = value

    print(max)


def run_loop(phase_setting):
    data = read_input("input.txt")[0]

    code_A = [int(d) for d in data.split(',')]
    code_B = [int(d) for d in data.split(',')]
    code_C = [int(d) for d in data.split(',')]
    code_D = [int(d) for d in data.split(',')]
    code_E = [int(d) for d in data.split(',')]

    codes = [code_A, code_B, code_C, code_D, code_E]
    ip = [0, 0, 0, 0, 0]
    input_values = [[phase_setting[0]], [phase_setting[1]], [phase_setting[2]], [phase_setting[3]], [phase_setting[4]]]
    input_values[0].append(0)

    current = 0
    result = 0
    while True:

        ip[current], codes[current], output, halt = perform_intruction(codes[current], ip[current], input_values[current])

        if halt:
            break

        if output is not None:
            result = output
            current = (current + 1) % len(codes)
            input_values[current].append(output)

    return result


def get_thruster_signal(phase_setting):
    signal = 0
    for phase in phase_setting:
        input_values = [phase, signal]

        output = runCode(input_values)

        signal = output[0]

    return signal


def runCode(input_values):

    data = read_input("input.txt")[0]

    code = [int(d) for d in data.split(',')]

    output = []
    i = 0
    while True:
        if code[i] == 99 or i >= len(code):
            break

        i, code, out = perform_intruction(code, i, input_values)

        if out is not None:
            output.append(out)

    return output


def perform_intruction(code, i, input_values):

    opcode = str(code[i])

    while len(opcode) < 5:
        opcode = '0' + opcode

    operation = int(opcode[3:])
    modes = [int(opcode[2]),int(opcode[1]),int(opcode[0])]

    if operation == 99:
        return i, code, None, True

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
        code[code[i+1]] = input_values.pop(0)
        i += 2

    if operation == 4:
        params = get_params(1)
        i += 2
        return i, code, params[0], False

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

    return i, code, None, False


def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task7_2()