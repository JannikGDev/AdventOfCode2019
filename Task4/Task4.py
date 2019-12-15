import numpy


def task4():
    low = 372037
    high = 905157

    guess = low
    amount = 0
    while guess <= high:

        if has_double_digit(guess) and never_decreases(guess) and has_one_exact_double(guess):
            amount += 1


        guess += 1


    print(amount)

def has_double_digit(number):

    word = str(number)

    for i in range(len(word)-1):

        if word[i] == word[i+1]:
            return True

    return False

def has_one_exact_double(number):

    word = str(number)
    last_match = False
    for i in range(len(word)-1):

        if word[i] == word[i+1]:
            left_free = False
            right_free = False

            if i == 0:
                left_free = True
            elif not word[i-1] == word[i]:
                left_free = True

            if i == len(word)-2:
                right_free = True
            elif not word[i+1] == word[i+2]:
                right_free = True


            if left_free and right_free:
                return True

    return False

def never_decreases(number):

    word = str(number)
    number = 0
    for i in range(len(word)):

        if int(word[i]) < number:
            return False

        number = int(word[i])

    return True


if __name__ == "__main__":
    task4()