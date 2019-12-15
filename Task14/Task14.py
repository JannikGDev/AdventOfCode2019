
def task14_1():

    data = read_input("input.txt")

    reactions = [parse_reaction(line) for line in data]
    reaction_index = dict()

    for reaction in reactions:
        reaction_index[reaction[1][1]] = reaction

    chemicals = dict()

    chemicals['FUEL'] = 1

    while True:
        keys = [key for key in chemicals.keys()]
        for key in keys:
            if key == 'ORE':
                continue

            required = get_required((chemicals[key], key), reaction_index)
            del chemicals[key]

            for chem in required:
                if chem[1] in chemicals:
                    chemicals[chem[1]] += chem[0]
                else:
                    chemicals[chem[1]] = chem[0]

    return


def get_required(chemical, reaction_index):

    reaction = reaction_index[chemical[1]]

    ingredients = [(chem[0]*chemical[0], chem[1]) for chem in reaction[0]]

    return ingredients



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
        amount = splitted[0]
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
    task14_1()
