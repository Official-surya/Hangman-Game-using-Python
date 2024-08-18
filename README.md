![Screenshot 2024-08-18 203435](https://github.com/user-attachments/assets/1a4d0a40-c80c-446f-8e41-f2465cafd9e6)### Hangman Game with Visualization <br>

Welcome to the Hangman Game! The Hangman word guessing game enhanced with visuals using Matplotlib and emojis, written in Python. Guess words in various categories from your friends, ask for a hint or see how well you do while completing. <br>

### Features <br>

1. **Variety of Categories:** — Fruits, Animals, Birds,…— Vegetable…-Computer Components and more ive. <br>
2. **Display Name:** Guesses are displayed with letter being color coded and displaying a symbol if the guess is correct or incorrect <br>
3. **Clues:** Players may ask for up to two clues which will highlight a letter in the secret word. <br>
4. **Visualization of Guesses:** Generates a bar chart showing number of correct and incorrect guesses directly after game is run. <br>
5. **Warnings/messages:** styled text for a more friendly user experience. <br>

### Prerequisites <br>
You will need following Python Libraries to run this project: <br>

1. **matplotlib :** To display correct and incorrect guesses. <br>
2. **colorama:** Makes some of these modules cross platform friendly by fixing Windows bugs for you. <br>
3. **emoji:** To flash emojis as alerts. <br>

## You can install the required libraries using pip: <br>
pip install matplotlib colorama emoji
<br>
### How to Play <br>

1. **Get the repository:** Clone this repo to your local machine. <br>
2. **Word Files :** You have text files ( fruits txt, animals. txt, birds. txt, computer_components. txt, vegetables. txt) where each category takes place on one line of a file.lineEdit. <br>
3. Execute hangman_game to run the game py script in your python shell. <br>
4. **Category:** Select a word category from the words you've been given. <br>
5. Guess the Word | Enter your letter guesses or ask for a hint Your goal is to guess the word before you use up all your attempts. <br>
6. Visualize: After every game, we will show a bar chart to view your guessed pubs. <br>

### Code Overview <br>
#### Main Functions <br>

1. **print_warning, print_warning1 and print_warning2 —** Functions for printing special warnings in the terminal. <br>
2. **def load_words_from_file(filename):** # Release words.txt file from the specified repository. <br>
3. **get_random_word(word_list):** This function will select any random word from the loaded list of words. <br>
4. **display_word(word, guessed_letters, wrong_guesses):** -> Void: Displays the current state of a word being guessed. <br>
5. **visualize_guesses(guess_sequence):** Make a bar chart visualization of correct and wrong guesses. <br>
6. **give_hint(word, guessed_letters):** Gives a hint by revealing encerando random letter from the word.<br>
7. **def play_hangman_game(word_list):** Main game loop — accepting guesses, providing hints, and displaying results. <br>
8. **HangManGame() :** This is a very important class having the flow of game such as selecting category and multiple games. <br>

### Output : <br>
#### Hangman_Game_bar:<br>
![image](https://github.com/user-attachments/assets/e0f81bbd-f04b-4dc8-af15-03096173904e)
![image](https://github.com/user-attachments/assets/31756fef-08c3-4aec-8a9d-2387c49c890b)
#### Hangman_Game_plot:<br>
![image](https://github.com/user-attachments/assets/d9641b8b-1be3-44fd-81ad-dbccdc39959a)


