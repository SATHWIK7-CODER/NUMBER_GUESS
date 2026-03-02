import random

def save_score(name, attempts, won):
    with open("scores.txt", "a") as file:
        if won:
            result = "Won"
        else:
            result = "Lost"
        file.write(f"{name} - {attempts} attempts - {result}\n")

def show_scores():
    print("\n--- HIGH SCORES ---")
    try:
        with open("scores.txt", "r") as file:
            content = file.read()
            if content:
                print(content)
            else:
                print("No scores yet!\n")
    except FileNotFoundError:
        print("No scores yet!\n")
    print("-------------------\n")

def choose_difficulty():
    print("Choose difficulty:")
    print("1. Easy   (10 attempts)")
    print("2. Medium (5 attempts)")
    print("3. Hard   (3 attempts)")
    difficulty = input("Enter choice (1/2/3): ")
    if difficulty == "1":
        return 10
    elif difficulty == "2":
        return 5
    elif difficulty == "3":
        return 3
    else:
        print("Invalid choice, setting Medium by default")
        return 5

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    user_guess = 0
    won = False

    max_attempts = choose_difficulty()
    print(f"\nI'm thinking of a number between 1 and 100...")
    print(f"You have {max_attempts} attempts! Good luck! 🎯\n")

    while user_guess != secret_number and attempts < max_attempts:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess == secret_number:
            won = True
            print(f"\nYou got it in {attempts} attempts! 🎉")
        elif user_guess < secret_number:
            print(f"Too low! {max_attempts - attempts} attempts left")
        else:
            print(f"Too high! {max_attempts - attempts} attempts left")

    if not won:
        print(f"\nGame Over! The number was {secret_number} 😢")

    return attempts, won

def main():
    print("🎮 WELCOME TO THE NUMBER GUESSING GAME! 🎮")

    while True:
        show_scores()

        name = input("Enter your name: ")

        attempts, won = play_game()

        save_score(name, attempts, won)

        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() == "no":
            print(f"\nThanks for playing {name}! Goodbye! 👋")
            break

main()