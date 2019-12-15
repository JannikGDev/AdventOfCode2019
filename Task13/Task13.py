from IntCode import IntCode
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from pynput.keyboard import Key, Listener

matplotlib.use('TkAgg')
plt.ion()



def task13_1():

    data = read_input("input.txt")[0]
    code = [int(d) for d in data.split(',')]

    program = IntCode(code)
    code[0] = 2
    score = 0

    global joystick
    joystick = 0

    screen = np.zeros((10, 10))

    def on_press(key):
        global joystick
        if key == Key.left:
            joystick = -1
            return False
        if key == Key.right:
            joystick = 1
            return False

        if key == Key.down:
            joystick = 0
            return False



    while not program.stopped:
        program.inputs = [joystick]
        program.run_until_expect_input()

        screen, n_score = update_screen(screen, program.outputs)

        program.outputs.clear()

        # Collect events until released
        with Listener(
                on_press=on_press) as listener:
            listener.join()

        if n_score is not None:
            score += score
            print(score)

    return


def update_screen(screen, outputs):
    score = None
    i = 0
    while i < len(outputs):

        if outputs[i] == -1 and outputs[i + 1] == 0:
            score = outputs[i + 2]
        else:
            screen = draw_screen(screen, outputs[i], outputs[i + 1], outputs[i + 2])

        i += 3

    plt.imshow(screen.transpose())
    plt.show()
    plt.pause(0.001)

    return screen, score


def draw_screen(screen, x, y, tile):

    if x >= screen.shape[0]:
        new_screen = np.zeros((screen.shape[0] + (x+1 - screen.shape[0]), screen.shape[1]))
        new_screen[:screen.shape[0], :screen.shape[1]] = screen
        screen = new_screen

    if y >= screen.shape[1]:
        new_screen = np.zeros((screen.shape[0], screen.shape[1] + (y+1 - screen.shape[1])))
        new_screen[:screen.shape[0], :screen.shape[1]] = screen
        screen = new_screen

    screen[x, y] = tile

    return screen


def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task13_1()
