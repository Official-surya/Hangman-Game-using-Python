import random
import matplotlib.pyplot as plt
from colorama import Fore, Style
import emoji

# Function to print warnings with specific styles
def print_warning(message):
    border = "+" + "-" * len(message) + "+"
    print(border)
    print(Fore.RED + Style.BRIGHT + message + Style.RESET_ALL)
    print(border)

def print_warning1(message):
    border = "+" + "-" * len(message) + "+"
    print(border)
    print(Fore.GREEN + Style.BRIGHT + message + Style.RESET_ALL)
    print(border)

def print_warning2(message):
    border = "+" + "-" * len(message) + "+"
    print(border)
    print(Fore.CYAN + Style.BRIGHT + message + Style.RESET_ALL)
    print(border)

# Function to read words from a text file
def load_words_from_file(filename):
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

# Function to choose a random word from the list
def get_random_word(word_list):
    return random.choice(word_list)

# Function to display the current state of the word with correct/incorrect guesses visualized
def display_word(word, guessed_letters, wrong_guesses):
    displayed_word = ''
    for i, letter in enumerate(word):
        if letter in guessed_letters:
            displayed_word += Fore.GREEN + letter + Style.RESET_ALL + ' '
        elif word[i] in wrong_guesses:
            displayed_word += Fore.RED + word[i] + Style.RESET_ALL + ' '
        else:
            displayed_word += '_ '
    return displayed_word.strip()

# Function to visualize correct and incorrect guesses with a line chart
def visualize_guesses(guess_sequence):
    x_labels = []
    y_values = []

    for i, (guess, is_correct) in enumerate(guess_sequence):
        x_labels.append(guess)
        y_values.append(1 if is_correct else 0)

    fig, ax = plt.subplots()

    # Plotting the line chart
    ax.plot(range(len(x_labels)), y_values, marker='o', color='blue', linestyle='-', linewidth=2, markersize=10)

    # Marking correct and incorrect guesses with different colors
    for i, is_correct in enumerate(y_values):
        ax.plot(i, is_correct, marker='o', color='green' if is_correct else 'red')

    ax.set_title('Guess Visualization')
    ax.set_xlabel('Guessed Letters')
    ax.set_ylabel('Correct (1) / Incorrect (0)')
    ax.set_xticks(range(len(x_labels)))
    ax.set_xticklabels(x_labels)
    plt.ylim(-0.5, 1.5)

    # Add a summary section
    correct_counts = y_values.count(1)
    incorrect_counts = y_values.count(0)
    summary_text = f"Correct: {correct_counts}, Incorrect: {incorrect_counts}"
    plt.figtext(0.99, 0.01, summary_text, horizontalalignment='right', fontsize=12, color='blue')

    plt.show()

# Function to give a hint (reveal a letter from the word)
def provide_hint(word, guessed_letters):
    hint_letter = random.choice([letter for letter in word if letter not in guessed_letters])
    guessed_letters.add(hint_letter)
    print(f"Hint: The word contains the letter '{hint_letter}'.")

# Function to play a single game of Hangman
def play_hangman_game(word_list):
    word = get_random_word(word_list)
    guessed_letters = set()
    wrong_guesses = set()
    guess_sequence = []
    attempts_left = len(word) + 2
    hints_used = 0  # Track the number of hints used
    max_hints = 2  # Limit the number of hints the user can use
    word_guessed = False

    print_warning2("Starting a new game of Hangman!")

    while attempts_left > 0:
        print(f"\nWord: {display_word(word, guessed_letters, wrong_guesses)}")
        print(f"Attempts left: {attempts_left} | Hints used: {hints_used}/{max_hints}")
        action = input("Guess a letter or type 'hint' for a hint: ").lower()

        if action == 'hint':
            if hints_used < max_hints:
                provide_hint(word, guessed_letters)
                hints_used += 1
            else:
                print_warning("You've used all your hints.")
            continue

        if action in guessed_letters or action in wrong_guesses:
            print("You already guessed that letter.")
        elif action in word:
            guessed_letters.add(action)
            guess_sequence.append((action, True))
            print(f"Correct guess! {emoji.emojize(':green_heart:')}")
        else:
            wrong_guesses.add(action)
            guess_sequence.append((action, False))
            print(f"Incorrect guess. {emoji.emojize(':broken_heart:')}")

        attempts_left -= 1

        if all(letter in guessed_letters for letter in word):
            word_guessed = True
            print_warning1(f"Congratulations! You guessed the word '{word}' correctly.")
            break

    if not word_guessed and attempts_left == 0:
        print_warning(f"Sorry, you've run out of attempts. The word was '{word}'.")

    visualize_guesses(guess_sequence)

# Main function to control the game flow
def hangman_game():
    category_options = {
        '1': ('Fruits', 'fruits.txt'),
        '2': ('Animals', 'animals.txt'),
        '3': ('Birds', 'birds.txt'),
        '4': ('Computer Components', 'computer_components.txt'),
        '5': ('Vegetables', 'vegetables.txt')
    }

    print_warning2("Select a category:")
    for key, (name, _) in category_options.items():
        print(f"{key}. {name}")

    category_choice = input(Fore.BLUE + "Enter the number corresponding to your choice: " + Style.RESET_ALL)

    if category_choice in category_options:
        category_name, filename = category_options[category_choice]
        word_list = load_words_from_file(filename)
        print(f"\nYou selected the category: {category_name}")
    else:
        print_warning("Invalid choice. Defaulting to 'Fruits'.")
        word_list = load_words_from_file('fruits.txt')

    try:
        total_games = int(input("How many times would you like to play the game? "))
    except ValueError:
        print_warning("Invalid number. Defaulting to 1 game.")
        total_games = 1

    for game_number in range(1, total_games + 1):
        print(f"\n--- Game {game_number} of {total_games} ---")
        play_hangman_game(word_list)

    print_warning1("Thank you for playing Hangman!")

# Run the game
if __name__ == "__main__":
    hangman_game()
