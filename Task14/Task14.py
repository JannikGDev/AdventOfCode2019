import math

def task14_2():

    data = read_input("input.txt")

    reactions = [parse_reaction(line) for line in data]
    reaction_index = dict()

    for reaction in reactions:
        if reaction[1][1] in reaction_index:
            assert False

        reaction_index[reaction[1][1]] = reaction

    target_ore = 1000000000000


    min_guess = 1
    max_guess = 1000000000000
    fuel_guess = 0

    # Binary search
    while True:
        if max_guess is None:
            fuel_guess = min_guess*2
        else:
            fuel_guess = math.floor((max_guess - min_guess) / 2) + min_guess

        ore = determine_ore_needed(reaction_index, fuel_guess)

        print(fuel_guess)

        if min_guess == max_guess-1:
            print(fuel_guess)
            return

        if ore > target_ore:
            max_guess = fuel_guess
        elif ore < target_ore:
            min_guess = fuel_guess





def determine_ore_needed(reaction_index, fuel_amount):

    chemicals = dict()
    leftovers = dict()

    chemicals['FUEL'] = fuel_amount

    while True:
        keys = [key for key in chemicals.keys()]
        for key in keys:
            if key == 'ORE':
                if len(keys) == 1:
                    return chemicals['ORE']
                continue

            if key in leftovers:
                left = leftovers[key] - chemicals[key]
                if left > 0:
                    leftovers[key] = left
                    del chemicals[key]
                    continue
                elif left < 0:
                    del leftovers[key]
                    chemicals[key] = -left
                if left == 0:
                    del chemicals[key]
                    del leftovers[key]
                    continue

            required, leftover = get_required((chemicals[key], key), reaction_index)

            if key in leftovers:
                leftovers[key] += leftover
            else:
                leftovers[key] = leftover

            del chemicals[key]

            for chem in required:
                if chem[1] in chemicals:
                    chemicals[chem[1]] += chem[0]
                else:
                    chemicals[chem[1]] = chem[0]


    return

def task14_1():

    data = read_input("input.txt")

    reactions = [parse_reaction(line) for line in data]
    reaction_index = dict()

    for reaction in reactions:
        if reaction[1][1] in reaction_index:
            assert False

        reaction_index[reaction[1][1]] = reaction

    chemicals = dict()
    leftovers = dict()

    chemicals['FUEL'] = 1


    while True:
        keys = [key for key in chemicals.keys()]
        for key in keys:
            if key == 'ORE':
                if len(keys) == 1:
                    print(chemicals['ORE'])
                    return
                continue

            if key in leftovers:
                left = leftovers[key] - chemicals[key]
                if left > 0:
                    leftovers[key] = left
                    del chemicals[key]
                    continue
                elif left < 0:
                    del leftovers[key]
                    chemicals[key] = -left
                if left == 0:
                    del chemicals[key]
                    del leftovers[key]
                    continue

            required, leftover = get_required((chemicals[key], key), reaction_index)

            if key in leftovers:
                leftovers[key] += leftover
            else:
                leftovers[key] = leftover

            del chemicals[key]

            for chem in required:
                if chem[1] in chemicals:
                    chemicals[chem[1]] += chem[0]
                else:
                    chemicals[chem[1]] = chem[0]

    return


def get_required(chemical, reaction_index):

    reaction = reaction_index[chemical[1]]

    amount = math.ceil(chemical[0]/reaction[1][0])

    ingredients = [(chem[0]*amount, chem[1]) for chem in reaction[0]]

    leftover = amount*reaction[1][0] - chemical[0]

    return ingredients, leftover


def parse_reaction(line: str):

    text = line.strip()
    parts = text.split("=>")
    result = parts[1].strip().split(" ")
    ingredients = parts[0].strip().split(",")

    result_amount = int(result[0])
    result_type = result[1]

    inputs = []
    output = (result_amount, result_type)

    for ingredient in ingredients:

        splitted = ingredient.strip().split(" ")
        amount = int(splitted[0])
        type = splitted[1]
        inputs.append((amount, type))

    reaction = (inputs, output)

    return reaction

def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data


if __name__ == "__main__":
    task14_2()
