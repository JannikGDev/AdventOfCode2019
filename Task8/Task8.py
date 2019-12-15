import numpy as np
import matplotlib.pyplot as plt

def task8_1():

    data = read_input("input.txt")
    pixels = [int(d) for d in data[0]]

    width = 25
    height = 6

    layer_size = width*height
    layer_amount = int(len(pixels)/layer_size)

    layers = [np.array(pixels[i*layer_size:(i+1)*layer_size]).reshape((width, height)) for i in range(layer_amount)]

    min_layer = find_min_amount_layer(layers, 0)

    ones = (min_layer == 1).sum()
    twos = (min_layer == 2).sum()
    result = ones*twos

    print(result)

def task8_2():

    data = read_input("input.txt")
    pixels = [int(d) for d in data[0]]

    width = 25
    height = 6

    layer_size = width*height
    layer_amount = int(len(pixels)/layer_size)

    layers = [np.array(pixels[i*layer_size:(i+1)*layer_size]).reshape((height, width)) for i in range(layer_amount)]

    image = stack_layers(layers)

    plt.imshow(image)
    plt.show()

def stack_layers(layers):

    image = np.ones(layers[0].shape)*2

    for layer in layers:

        image = (image != 2)*image + (image == 2)*layer

    return image



def find_min_amount_layer(layers, digit: int):

    min = 0
    min_layer = None

    for layer in layers:

        amount = (layer == digit).sum()

        if min_layer is None or amount < min:
            min = amount
            min_layer = layer

    return min_layer





def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task8_2()