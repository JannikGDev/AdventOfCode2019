from IntCode import IntCode
import numpy as np


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
    task17_1()
