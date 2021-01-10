import random as rn


def generate_num(minNum: int, maxNum: int):
    '''Generate random number from range
    '''
    return rn.randint(minNum, maxNum)


def make_guess(guessList: list, hint: str):
    '''Make a guess based on the list of previous guesses and hint
    '''
    pass


def check_guess(num: int, guess: int):
    if num == guess:
        return True
    else:
        return False


def give_hint(guessList: list, hint: str):
    '''
    Guessing number based on previous guesses
    '''
    if hint == "hot":
        pass


def main_process():
    count = 0
    while True:
        count += 1
        num = generate_num()
        guess = generate_num()
        if num == guess:
            break
        else:
            continue
    return count


if __name__ == "__main__":
    count = []
    for x in range(100000):
        count.append(main_process())
    print(sum(count)/len(count))
