import random as rn


def generate_num(minNum: int, maxNum: int):
    '''Generate random number from range
    '''
    return rn.randint(minNum, maxNum)


def make_guess(guessList: list, hint: str, minNum: int, maxNum: int):
    '''Make a guess based on the list of previous guesses and hint
    '''
    while True:
        if hint == "hot":
            last_guess = guessList[-1]
            before_last_guess = guessList[-2]
            if last_guess > before_last_guess:
                minNum = int((last_guess + before_last_guess)/2)
            elif last_guess < before_last_guess:
                maxNum = int((last_guess + before_last_guess)/2)
        elif hint == "cold":
            last_guess = guessList[-1]
            before_last_guess = guessList[-2]
            if last_guess < before_last_guess:
                minNum = int((last_guess + before_last_guess)/2)
            elif last_guess > before_last_guess:
                maxNum = int((last_guess + before_last_guess)/2)
        guess = rn.randint(minNum, maxNum)  # make a guess
        
        if guess not in guessList:
            guessList.append(guess)
            return guess, guessList, minNum, maxNum


def check_guess(num: int, guess: int):
    '''Check if the guess was correct
    '''
    if num == guess:
        return True
    else:
        return False


def give_hint(guessList: list, num: int):
    '''Give a hint based on the missed guess compared to the before last guess
    '''
    if len(guessList) >= 2:
        last_guess = guessList[-1]
        before_last_guess = guessList[-2]
        last_guess_proximity = abs(num - last_guess)
        before_last_guess_proximity = abs(num - before_last_guess)
        if last_guess_proximity < before_last_guess_proximity:
            return "hot"
        elif last_guess_proximity > before_last_guess_proximity:
            return "cold"
    else:
        return ""


def main_process(minNum: int, maxNum: int):
    count = 0
    num = generate_num(minNum, maxNum)
    guessList = []
    hint = ""
    while True:
        count += 1
        guess, guessListm, minNum, maxNum = make_guess(guessList, hint, minNum, maxNum)
        if check_guess(num, guess):
            break
        else:
            hint = give_hint(guessList, num)
            continue
    return count


if __name__ == "__main__":
    count = []
    for x in range(10000):
        count.append(main_process(1, 100))
    print(sum(count)/len(count))
