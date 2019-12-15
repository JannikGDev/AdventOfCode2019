from IntCode import IntCode
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def task13_1():

    data = read_input("input.txt")[0]
    code = [int(d) for d in data.split(',')]

    program = IntCode(code)
    code[0] = 2
    score = 0

    joystick = 0

    screen = np.zeros((10, 10))
    step = 0
    while not program.stopped:
        program.inputs = [joystick]
        program.run_until_expect_input()

        screen, n_score = update_screen(screen, program.outputs)
        program.outputs.clear()

        paddle_pos = np.where(screen == 3)
        paddle_pos = [paddle_pos[0][0], paddle_pos[1][0]]

        ball_pos = np.where(screen == 4)
        ball_pos = [ball_pos[0][0], ball_pos[1][0]]

        joystick = game_ai(ball_pos, paddle_pos)

        if n_score is not None:
            score = n_score

        step += 1
        if step % 100 == 0:
            print(step)

    print("FINAL SCORE: " + str(score))

    return


def game_ai(ball_pos, self_pos):

    if ball_pos[0] > self_pos[0]:
        return 1
    elif ball_pos[0] < self_pos[0]:
        return -1

    return 0


def update_screen(screen, outputs):
    score = None
    i = 0
    while i < len(outputs):

        if outputs[i] == -1 and outputs[i + 1] == 0:
            score = outputs[i + 2]
        else:
            screen = draw_screen(screen, outputs[i], outputs[i + 1], outputs[i + 2])

        i += 3

    return screen, score


def show_screen(screen):

    plt.imshow(screen.transpose())
    plt.show()
    plt.pause(0.001)

    return

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
