from typing import *
from Task11.IntCode import IntCode
import numpy as np
import matplotlib.pyplot as plt

def task11():

    data = read_input("input.txt")[0]
    code = [int(d) for d in data.split(',')]

    program = IntCode(code)

    field = {}
    field[0] = {}
    field[0][0] = 1
    robot_x = 0
    robot_y = 0
    robot_dir = 0

    while True:
        current_field = read_field(field,robot_x,robot_y)

        program.run_until_output(input_values=[current_field])
        if len(program.outputs) == 0:
            break
        color = program.outputs.pop(0)
        set_field(field, robot_x, robot_y, color)

        program.run_until_output(input_values=[])
        if len(program.outputs) == 0:
            break
        turn_dir = program.outputs.pop(0)

        robot_dir = (robot_dir + (-1 + turn_dir*2)) % 4

        if robot_dir == 0:
            robot_y += 1
        elif robot_dir == 1:
            robot_x += 1
        elif robot_dir == 2:
            robot_y += -1
        elif robot_dir == 3:
            robot_x += -1

    max = 0
    min = 0
    for x in field.keys():
        for y in field[x].keys():
            if x > max:
                max = x
            if x < min:
                min = x
            if y > max:
                max = y
            if y < min:
                min = y

    image = np.zeros((max-min+1,max-min+1))

    for x in field.keys():
        for y in field[x].keys():
            image[x-min][y-min] = field[x][y]

    plt.imshow(image)
    plt.show()

    return

def read_field(field,x,y):

    if x not in field:
        return 0

    if y not in field[x]:
        return 0

    return field[x][y]

def set_field(field,x,y, value):

    if x not in field:
        field[x] = {}

    if y not in field[x]:
        field[x][y] = 0

    field[x][y] = value




def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task11()
















