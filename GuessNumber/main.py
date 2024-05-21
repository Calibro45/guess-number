# Number Guessing Game Objectives:
import random

from art import logo

print(logo)

print("Welcome to the number guessing game!")


# pick a random number between 1 to 100
def generate_random_number():
    random_number = random.randint(1, 100)
    # print(f"Pss the number is {random_number}")
    return random_number


def set_game_difficulty():
    ''' Set the difficulty of the game and return the attempt for guessing number '''
    choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if choose_difficulty == "easy":
        attempt = 10
    elif choose_difficulty == "hard":
        attempt = 5
    else:
        return print("Gmae Over")
    return attempt


def game():
    ''' Function start the game '''
    print("I'm thinking of a number between 1 and 100.")

    RANDOM_NUMBER = generate_random_number()
    game_attempt = set_game_difficulty()
    user_guess = 0

    while user_guess != RANDOM_NUMBER and game_attempt > 0:

        print(f"You have {game_attempt} attemps remaining to guess the number.")

        user_guess = int(input("Make a guess: "))

        def check_number(random, user_number, score):
            ''' Check the user number with random number and compare them '''
            if random > user_number:
                print("Too low.")
                return score - 1
            elif random < user_number:
                print("Too higth.")
                return score - 1
            else:
                return

        game_attempt = check_number(RANDOM_NUMBER, user_guess, game_attempt)

        if game_attempt == 0:
            print("You're run out of attempt.")
        elif user_guess != RANDOM_NUMBER:
            print("Guess again")
        else:
            print(f"You got it the answer is: {RANDOM_NUMBER}")

    play_again = input("You want to play again?. Type 'y' or 'n':    ").lower()

    if play_again == "y":
        game()


game()
