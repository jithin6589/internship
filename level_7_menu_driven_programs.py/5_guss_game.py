import random


def play_game():

    secret_number = random.randint(1, 100)
    print(secret_number)

    guess_count = 0

    while True:

        user_guess = int(input("Enter your guess: "))

        guess_count = guess_count + 1

        if user_guess < secret_number:
            print("Higher!")

        elif user_guess > secret_number:
            print("Lower!")

        else:
            print("Correct!")
            print("You guessed it in", guess_count, "guesses.")
            break

    return guess_count


def main():

    high_score = None

    while True:

        print("\n1. Play Game")
        print("2. View High Score")
        print("3. Exit")

        try:

            choice = int(input("Enter your choice: "))

            if choice == 1:

                guess_count = play_game()

                if high_score is None or guess_count < high_score:
                    high_score = guess_count
                    print("New High Score!")

            elif choice == 2:

                if high_score is None:
                    print("No high score yet.")

                else:
                    print("High Score:", high_score, "guesses")

            elif choice == 3:

                print("Game exited.")
                break

            else:

                print("Invalid choice. Please enter 1 to 3.")

        except ValueError:

            print("Invalid input. Please enter a number.")


main()