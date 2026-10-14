import constants


def main():

    # Get a guessed nunber from the user
    guessed = int(input("Guess a random number in the range of 0-9: "))

    # check if the mumber is the same as the correct number

    if guessed == constants.CORRECT_NUMBER:

        # If correct then tell the user they guessed correct
        print("You Guessed Correct!")

    if guessed != constants.CORRECT_NUMBER:

        # If not correct then tell the user they guessed incorrect
        print("You Guessed incorrect!")


if __name__ == "__main__":
    main()
