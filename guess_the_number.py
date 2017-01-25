import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'
min_range = 1
max_range = 100


def configure_range():
    '''Set the high and low values for the random number'''

    while True:

        try:
            low = 0

            while low <= min_range or low >= max_range:

                low = int(input("Enter low end of guessing range. Must be > {}  and < {} \n".format(min_range, max_range)))

            break

        except ValueError:

            print("Did you enter a number?")

    while True:

        try:
            high = 0

            while high >= 100 or high <= low:

                high = int(input("Enter high end of guessing range. must be > {}  and < {} \n".format(low, max_range)))

            break

        except ValueError:

            print("Did you enter a number?")

    return low, high


def generate_secret(low, high):
    '''Generate a secret number for the user to guess'''
    return random.randint(low, high)


def get_guess():
    '''get user's guess'''
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    '''compare guess and secret, return string describing result of comparison'''
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():

    #variable to track number of guesses made
    numOfGuesses = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        #add one every time a guess is made to track guesses
        numOfGuesses += 1
        guess = get_guess()
        result = check_guess(guess, secret)
        print(result)
        #print number of guesses
        print('You have guessed ' + str(numOfGuesses) + ' times')
        if result == correct:
            break


if __name__ == '__main__':

    option = input("\nPress Any Key To Start. Press Q To Quit.\n")

    while option.lower() != "q":

        main()

        menu = input("\nPlay Game? Press any Key. Press Q to Quit.\n")

    exit()
