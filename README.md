# HangMan
 Guess the right word!! Be careful though, as you only have 5 chances to figure the word out at the cost of an innocent man getting hanged :(

Break down of the the code step by step:

1. **Welcome Function (`welcome()`)**:
   - This function prompts the user to enter their name.
   - It runs in a loop (`while True`) until a valid name (containing only alphabetic characters) is entered.
   - If the entered name is valid, it prints a welcome message including the name and some game instructions.
   - If the entered name is invalid (e.g., contains non-alphabetic characters), it prompts the user again.

2. **Play Again Function (`play_again()`)**:
   - This function asks the user if they want to play the game again after completing a round.
   - It takes user input (`response`) to determine if the user wants to play again.
   - If the user enters 'Y' (case insensitive), it calls the `game_run()` function to start a new game.
   - If the user enters anything else, it prints a farewell message.

3. **Get Word Function (`get_word()`)**:
   - This function generates a random word for the user to guess.
   - It selects a word randomly from a predefined list of words and returns it in lowercase.

4. **Game Run Function (`game_run()`)**:
   - This function orchestrates the entire game.
   - It first calls the `welcome()` function to get the player's name and display game instructions.
   - It initializes variables such as `alphabet` (containing all lowercase letters), `word` (the word to be guessed), `letters_guessed` (a list to store guessed letters), and `tries` (number of attempts allowed).
   - It enters a loop where the player can guess letters or the entire word.
   - Inside the loop, it checks the validity of the guess (whether it's a single letter or the entire word) and updates the game state accordingly.
   - If the player guesses the entire word correctly or runs out of tries, it ends the game and asks if the player wants to play again by calling the `play_again()` function.

5. **Full Program Run**:
   - It simply calls the `game_run()` function to start the game when the script is executed.

This script creates a simple Hangman game where the player guesses letters or the entire word within a limited number of tries. After each round, the player is prompted if they want to play again.