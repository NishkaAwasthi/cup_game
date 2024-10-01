import random

def generate_random_order():
    # Generate an array of numbers from 1 to 5 and shuffle it
    array = [1, 2, 3, 4, 5]
    random.shuffle(array)
    return array

def get_correct_placements(secret_order, user_guess):
    # Count how many numbers are in the correct position
    correct_count = 0
    for i in range(len(secret_order)):
        if secret_order[i] == user_guess[i]:
            correct_count += 1
    return correct_count

def get_user_guess():
    # Get the user's guess as a list of integers
    while True:
        guess = input("Enter your guess (e.g., 1 2 3 4 5): ")
        guess_list = guess.split()
        
        # Check if the input is valid
        if len(guess_list) != 5:
            print("\n[Error] Please enter exactly 5 numbers.\n")
            continue
        try:
            guess_list = list(map(int, guess_list))
        except ValueError:
            print("\n[Error] Please enter only numbers.\n")
            continue
        
        if sorted(guess_list) != [1, 2, 3, 4, 5]:
            print("\n[Error] You must enter all numbers from 1 to 5 without repeating.\n")
            continue
        
        return guess_list

def print_welcome_message():
    print("="*40)
    print(" Welcome to the Number Ordering Game! ".center(40))
    print("="*40)
    print("\nInstructions: Your goal is to guess the correct order of the numbers 1 through 5.")
    print("After each guess, you'll be told how many numbers are in the correct position.")
    print("Try to guess the correct order in as few attempts as possible!\n")
    print("-"*40)

def print_congratulations(secret_order, attempts):
    print("\n" + "="*40)
    print(" Congratulations! You've guessed the correct order! ".center(40))
    print("="*40)
    print(f"\nIt took you {attempts} attempt(s) to guess the correct order.")
    print(f"The correct order was: {secret_order}\n")

def main():
    print_welcome_message()

    secret_order = generate_random_order()
    attempts = 0
    correct_placement = 0

    while correct_placement != 5:
        print("\n" + "-"*40)
        user_guess = get_user_guess()
        correct_placement = get_correct_placements(secret_order, user_guess)
        attempts += 1
        print(f"Your guess: {user_guess}")
        print(f"Correctly placed numbers: {correct_placement}")
        print("-"*40)

    print_congratulations(secret_order, attempts)

if __name__ == "__main__":
    main()
