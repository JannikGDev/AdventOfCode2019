from typing import List


class IntCode:

    def __init__(self, code, instruction_pointer: int = 0, rel_base: int = 0):

        self.code: List = code
        self.rel_base = rel_base
        self.i = instruction_pointer
        self.outputs = []
        self.inputs = []
        self.stopped = False
        self.expect_input = False

    def get(self, index):

        if index >= len(self.code):
            self.code.extend([0 for j in range((index+1) - len(self.code))])

        return self.code[index]

    def set(self, index, value):

        if index >= len(self.code):
            self.code.extend([0 for j in range((index+1) - len(self.code))])

        self.code[index] = value

    def run_until_stop(self, input_values: List = []):

        self.inputs = input_values

        while not self.stopped:
            self.step()

    def run_until_output(self, input_values: List = []):

        self.inputs = input_values

        while len(self.outputs) == 0 and not self.stopped:
            self.step()

    def run_until_expect_input(self, input_values: List = []):

        self.inputs.extend(input_values)

        while not (self.expect_input and len(self.inputs) == 0) and not self.stopped:
            self.step()

    def step(self):
        if self.stopped:
            return

        i = self.i
        rel_base = self.rel_base

        opcode = str(self.get(i))

        while len(opcode) < 5:
            opcode = '0' + opcode

        operation = int(opcode[-2:])
        modes = [int(opcode[2]), int(opcode[1]), int(opcode[0])]

        if operation == 99:
            self.stopped = True
            return

        def get_write_addr(rel_index):

            if modes[rel_index] == 2:
                return self.get(self.i + rel_index + 1) + rel_base
            else:
                return self.get(self.i + rel_index + 1)

        def get_params(amount):
            values = []

            for j in range(amount):
                if modes[j] == 2:
                    # Relative Mode
                    values.append(self.get(self.get(i + j + 1) + rel_base))
                elif modes[j] == 1:
                    # Immediate Mode
                    values.append(self.get(i + j + 1))
                elif modes[j] == 0:
                    # Position Mode
                    values.append(self.get(self.get(i + j + 1)))

            return values

        # Add
        if operation == 1:
            params = get_params(2)
            self.set(get_write_addr(2), params[1] + params[0])
            i += 4

        # Multiply
        if operation == 2:
            params = get_params(2)
            self.set(get_write_addr(2), params[1] * params[0])
            i += 4

        # Read Input
        if operation == 3:
            pass
            if len(self.inputs) > 0:
                self.expect_input = False
                self.set(get_write_addr(0), self.inputs.pop(0))
                i += 2
            else:
                self.expect_input = True


        # Write Output
        if operation == 4:
            params = get_params(1)
            i += 2
            self.outputs.append(params[0])

        # Jump if true
        if operation == 5:
            params = get_params(2)
            if params[0] != 0:
                i = params[1]
            else:
                i += 3

        # Jump if false
        if operation == 6:
            params = get_params(2)
            if params[0] == 0:
                i = params[1]
            else:
                i += 3

        # Less than
        if operation == 7:
            params = get_params(2)
            if params[0] < params[1]:
                self.set(get_write_addr(2), 1)
            else:
                self.set(get_write_addr(2), 0)

            i += 4

        # equals
        if operation == 8:
            params = get_params(2)
            if params[0] == params[1]:
                self.set(get_write_addr(2), 1)
            else:
                self.set(get_write_addr(2), 0)

            i += 4

        # Modify Rel_Base
        if operation == 9:
            params = get_params(1)
            rel_base += params[0]
            i += 2

        self.i = i
        self.rel_base = rel_base

        return
