from IntCode import IntCode
import numpy as np
import math

SCAFFOLG = '#'
EMPTY = '.'
ROBOT_LEFT = "<"
ROBOT_DOWN = "v"
ROBOT_UP = "^"
ROBOT_RIGHT = ">"
ROBOT_FREE = "X"



def task17_1():
    data = read_input("input.txt")[0]
    code = [int(d) for d in data.split(',')]

    program = IntCode(code)

    program.run_until_stop()
    output = program.outputs

    map = []
    line = []
    for o in output:
        ch = chr(o)

        if ch == '\n':
            if len(line) > 0:
                map.append(line)
                line = []
        else:
            line.append(ch)

    map = np.array(map)

    crossings = find_crossings(map)

    alignment_sum = 0

    for crossing in crossings:

        alignment_sum += crossing[0]*crossing[1]

    print(alignment_sum)
    return


def encode_ascii(string):

    ascii = []

    for letter in string:
        ascii.append(ord(letter))

    return ascii

def decode_ascii(codes):

    msg = ""

    for code in codes:
        msg = msg + chr(code)

    return msg


def task17_2():
    data = read_input("input.txt")[0]
    code = [int(d) for d in data.split(',')]

    code[0] = 2

    program = IntCode(code)

    program.run_until_expect_input(input_values=encode_ascii("B,A,B,A,C,C,A,B,C,B\n"))

    if len(program.outputs) > 0:
        print(decode_ascii(program.outputs))
        program.outputs.clear()

    program.run_until_expect_input(input_values=encode_ascii("L,12,R,8,L,12\n"))

    if len(program.outputs) > 0:
        print(decode_ascii(program.outputs))
        program.outputs.clear()

    program.run_until_expect_input(input_values=encode_ascii("L,10,R,8,R,6,R,10\n"))

    if len(program.outputs) > 0:
        print(decode_ascii(program.outputs))
        program.outputs.clear()

    program.run_until_expect_input(input_values=encode_ascii("L,10,R,8,R,8\n"))

    if len(program.outputs) > 0:
        print(decode_ascii(program.outputs))
        program.outputs.clear()

    program.run_until_stop(input_values=encode_ascii("n\n"))

    if len(program.outputs) > 0:

        output = program.outputs
        print(output[len(output)-1])
        program.outputs.clear()


    return

    """
    program.run_until_stop()
    output = program.outputs

    map = []
    line = []
    for o in output:
        ch = chr(o)

        if ch == '\n':
            if len(line) > 0:
                map.append(line)
                line = []
        else:
            line.append(ch)
    
    map = np.array(map)

    with open("map.txt",'w+') as file:
        for line in map:
            file.write("".join(line) + "\n")

    move_path: str = "".join(read_input("instructions.txt"))
    move_path = move_path.replace(" ", "")
    move_path = move_path.replace("\n", "")
    move_path = move_path.split(",")
    move_path = [(move_path[i*2], move_path[i*2+1]) for i in range(math.ceil(len(move_path)/2))]

    patterns = find_patterns(move_path)

    return
    """


def find_patterns(move_path):
    patterns = []

    for j in range(2, len(move_path)):
        for i in range(len(move_path)-(j-1)):
            pattern_count = 0
            pattern = move_path[i:i+j]

            for k in range(len(move_path) - (j - 1)):

                if lists_equal(pattern, move_path[k:k+j]):
                    pattern_count += 1

            patterns.append((pattern, pattern_count))

    better_patterns = []

    for pattern in patterns:

        if len(pattern[0]) > 1 and pattern[1] > 1:
            better_patterns.append(pattern)

    return better_patterns

def lists_equal(listA, listB):

    if not len(listA) == len(listB):
        return False


    for i in range(len(listA)):

        if not listA[i] == listB[i]:
            return False

    return True


def find_crossings(map):

    crossings = []

    for x in range(map.shape[0]):
        for y in range(map.shape[1]):

            if x >= 1 and x < map.shape[0]-1 and y >= 1 and y < map.shape[1]-1:

                if map[x][y] == '#' and \
                   map[x-1][y] == '#' and \
                   map[x+1][y] == '#' and \
                   map[x][y-1] == '#' and \
                   map[x][y+1] == '#':
                    crossings.append([x, y])

    return crossings




def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task17_2()
