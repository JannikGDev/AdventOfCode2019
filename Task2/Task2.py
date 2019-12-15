


def part_one(x, y):

    data = read_input("input.txt")

    line = data[0].split(",")
    code = [int(num) for num in line]

    code[1] = x
    code[2] = y

    i = 0
    while True:

        if code[i] == 99 or i >= len(code):
            break

        if code[i] == 1:

            code[code[i+3]] = code[code[i+1]] + code[code[i+2]]
            i += 4

        if code[i] == 2:
            code[code[i+3]] = code[code[i+1]] * code[code[i+2]]
            i += 4

    return code[0]


def part_two():

    for x in range(0,100):
        for y in range(0,100):
            result = part_one(x,y)

            if result == 19690720:
                print("X:" + str(x))
                print("Y:" + str(y))


class VariableExp:

    def __init__(self, variables):

        self.summand = 0
        self.factors = [1.0 for var in variables]
        self.variables = variables

    def __str__(self):
        text = ""

        for var, factor in zip(self.variables, self.factors):
            text += " " + str(factor) + "*" + str(var)
        text += " + "+str(self.summand)

        return text

# (X*a + b) + (X*c + d) = X*(a+b) + (b+d)
def add_var_exp(A: VariableExp, B: VariableExp):

    variables = A.variables
    if len(B.variables) > len(A.variables):
        variables = B.variables

    result = VariableExp(variables)

    result.summand = A.summand + B.summand
    factors = []
    for i in range(len(result.factors)):
        a = 0
        b = 0

        if i < len(A.factors):
            a = A.factors[i]
        if i < len(B.factors):
            b = B.factors[i]

        factors.append(a+b)

    result.factors = factors

    return result

# (X*a + b) * (X*c + d) = X*X*a*
def add_var_exp(A: VariableExp, B: VariableExp):

    variables = A.variables
    if len(B.variables) > len(A.variables):
        variables = B.variables

    result = VariableExp(variables)

    result.summand = A.summand + B.summand
    factors = []
    for i in range(len(result.factors)):
        a = 0
        b = 0

        if i < len(A.factors):
            a = A.factors[i]
        if i < len(B.factors):
            b = B.factors[i]

        factors.append(a+b)

    result.factors = factors

    return result







def read_input(path):

    input_data = []
    with open(path) as file:
        for line in file:
            input_data.append(line)

    return input_data

if __name__ == "__main__":
    part_two()