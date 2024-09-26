import random

def choose_difficulty():
    print("Choose a difficulty level:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 10 attempts)")
    
    while True:
        choice = input("Enter difficulty level (1, 2, or 3): ")
        if choice == '1':
            return 10, 5 
        elif choice == '2':
            return 50, 7 
        elif choice == '3':
            return 100, 10 
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

def get_user_guess():
    while True:
        guess = input("Enter your guess: ")
        if guess.isdigit():
            return int(guess)
        else:
            print("Please enter a valid number.")

def provide_hint(number_to_guess, attempts):
    if attempts == 3:
        if number_to_guess % 2 == 0:
            print("Hint: The number is even.")
        else:
            print("Hint: The number is odd.")

def play_game():
    print("Welcome to the Number Guessing Game!")
    range_limit, max_attempts = choose_difficulty()
    number_to_guess = random.randint(1, range_limit)
    attempts = 0
    score = 100  # Starting score

    while attempts < max_attempts:
        guess = get_user_guess()
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            print(f"Your score: {score - (attempts - 1) * 10}")
            break

        provide_hint(number_to_guess, attempts)

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts! The number was {number_to_guess}.")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
