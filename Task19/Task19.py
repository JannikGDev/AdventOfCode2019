from IntCode import IntCode
import numpy as np
import matplotlib.pyplot as plt
import math

def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data

data = read_input("input.txt")[0]
code = [int(d) for d in data.split(',')]
program = IntCode(code)

ray_left =(1, 1)
ray_right = (1, 1)

BOX_SIZE = 100

def task19():

    global ray_left
    global ray_right

    y = 10
    for i in range(20):
        left_edge = find_left_edge(y)
        ray_left = (left_edge, y)
        right_edge = find_right_edge(y)
        ray_right = (right_edge, y)

        y *= 2
    print("ACCURACY: " + str(y))

    best_guess_y = math.ceil(reverse_calc_box_space(BOX_SIZE))
    best_guess_x = find_right_edge(best_guess_y)

    # Check if there is better solution
    y = best_guess_y - 1
    while True:
        x = find_right_edge(y)
        if not (check_point(x, y) and check_point(y - (BOX_SIZE-1), y + (BOX_SIZE-1))):
            break
        else:
            best_guess_y = y
            best_guess_x = x

        y -= 1

    # Check solution, check if box can be moved left
    while check_point(best_guess_x-1, best_guess_y) and check_point(best_guess_x-1 - (BOX_SIZE), best_guess_y + (BOX_SIZE)):
        best_guess_x -= 1

    if not (check_point(best_guess_x, best_guess_y) and check_point(best_guess_x - BOX_SIZE, best_guess_y + BOX_SIZE)):
        print("FAIL")


    print(check_point(best_guess_x, best_guess_y))
    print(check_point(best_guess_x-BOX_SIZE, best_guess_y+BOX_SIZE))

    print(best_guess_x - (BOX_SIZE-1))
    print(best_guess_y)
    solution = (best_guess_x - (BOX_SIZE-1)) * 10000 + best_guess_y
    print(solution)

    print_box_in_ray(best_guess_x-200, best_guess_x+100, best_guess_y-100, best_guess_y+200, best_guess_x, best_guess_y, BOX_SIZE)
    return


def reverse_calc_ray_size(size):

    return size / (ray_right[0]/ray_right[1] - ray_left[0]/ray_left[1])

def reverse_calc_box_space(box_size):

    l = ray_left[0]/ray_left[1]
    r = ray_right[0]/ray_right[1]

    return (-box_size * (l + 1)) / (l - r)

def ray_heuristic(y, dx, dy):
    return round(dx*(y/dy))


def print_box_in_ray(start_x, end_x, start_y, end_y, right, top, box_size):
    grid = np.zeros((end_x - start_x, end_y - start_y))

    for y in range(start_y, end_y):
        left_edge = find_left_edge(y)
        right_edge = find_right_edge(y)
        x1 = max(left_edge-start_x, 0)
        x2 = max(right_edge - start_x + 1, 0)
        y1 = y - start_y
        grid[x1:x2, y1] = 1

    x1 = max(right-box_size-start_x, 0)
    x2 = max(right-start_x, 0)
    y1 = max(top-start_y, 0)
    y2 = max(top+box_size-start_y, 0)
    grid[x1:x2, y1:y2] = (grid[x1:x2, y1:y2]-1)*4 + 2

    print(grid.min())
    plt.imshow(grid.transpose())
    plt.show()


def print_ray_outline(size):
    grid = np.zeros((size, size))

    for y in range(size):
        left_edge = find_left_edge(y)
        right_edge = find_right_edge(y)
        grid[left_edge:right_edge+1, y] = 1

    plt.imshow(grid.transpose())
    plt.show()


def paint_ray(size):

    grid = np.zeros((size, size))

    for x in range(size):
        for y in range(size):
            grid[x, y] = check_point(x, y)

    plt.imshow(grid.transpose())
    plt.show()


def find_left_edge(y):

    d = 0
    guess = ray_heuristic(y, *ray_left)

    while True:
        x = guess + d

        if check_point(x, y) and (not check_point(x - 1, y) or x == 0):
            return x

        x = guess - d
        if x >= 0:
            if check_point(x, y) and (not check_point(x - 1, y) or x == 0):
                return x

        d += 1


def find_right_edge(y):

    d = 0
    guess = ray_heuristic(y, *ray_right)

    while True:
        x = guess + d

        if check_point(x, y) and (not check_point(x + 1, y) or x == 0):
            return x

        x = guess - d
        if x >= 0:
            if check_point(x, y) and (not check_point(x + 1, y) or x == 0):
                return x

        d += 1


def check_point(x, y):

    program.reset()
    program.run_until_output(input_values=[x, y])

    if program.outputs.pop(0) == 1:
        return True
    else:
        return False





if __name__ == "__main__":
    task19()
