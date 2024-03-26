#importing random module
import random
import requests

def welcome():
    while True:
        # Prompt the user to enter their name
        name = input("Welcome to Hangman Game!! Please enter your name, or not, I ain't your mama: ")

        # Check if a valid name is entered
        if name.isalpha():
            print("AYEEEE!", name, "My Mannn!! or woman, or a unicorn etc. <<< Rules simple. Computer picks a random word and you guess it, using a single letter or the whole word. Easy right? So have fun! OH! and you only get 7 chances to guess else you're the reason why an innocent man gets hanged right in front of you! So, have fun! >>>")
            break  # Exit the loop if a valid name is entered
        else:
            print("Mate... You ain't got no option, type yo name.")

#Define another function PLAY_AGAIN
#Add a doctring
def play_again():

        """This function asks user/player if they wish to replay the game"""
        response = input("Would you like to play again? Enter 'Y' for yes, 'N' for No: ").lower()

        #Create a decision making process
        if response == 'y':
                game_run()
        else:
                print('You snoooooze, you looooose, see yah')

#Define another function GET_WORD for generating random words for the user to guess
#Add a docstring

# Global variable to store the word
word_to_guess = None

def get_word():
    """This function generates the word the user will attempt guessing"""
    global word_to_guess
    if word_to_guess:
        return word_to_guess

    response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
    if response.status_code == 200:
        word = response.json()[0]
        word_to_guess = word.lower()
        return word_to_guess
    else:
        # If fetching fails, fallback to a local list of words
        words = ['python', 'cool', 'battery', 'urban', 'meow']
        word_to_guess = random.choice(words).lower()
        return word_to_guess
    
# Get the word
word_to_guess = get_word()

#Define another function DRAW_HANGMAN()
#Add docstring
def draw_hangman(incorrect_guesses):
    stages = [  # Hangman stages
        '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[incorrect_guesses]

# Example usage
incorrect_guesses = 6
print(incorrect_guesses)


#Define another function GAME_RUN(), add docstring if required
def game_run():
        """This function runs the game when invoked and basically call all the other functions that involves to be able to play this game"""
        
        #Call the 'WELCOME" function here to get the game running
        welcome()
        
        #Define an 'ALPHABET' variable
        alphabet = ('abcdefjhijklmnopqrstuvwxyz')
        
        #Set guess word to get_word function for a random word to be generated
        word = get_word()

        #Initiate an empty list for guessed letter
        letters_guessed = []
        
        #Initiate a tries variable for number of trues by the user
        tries = 7
        
        #Set initial guess to false
        guessed = False
        
        #print an empty line
        print()
        
        #print a guess hint for the user for number of letters contained in the word
        print('The word contains', len(word), 'letters.')
        print(len(word) * '_')
        
        #Initiate a while loop to create decisions, taking into consideration if the user decides to enter just a single letter or the full word
        while guessed == False and tries >0:
                print('You have '+str(tries)+' tries')
                guess = input('Guess a letter in the word or enter the full word. ').lower()
        #Create decisions for if user inputs a wrong entry and if the input letters is not equal to the total number of letters in the word to guess
        #user inputs letter
                if len(guess) == 1:
                        if guess not in alphabet:
                                print(draw_hangman(incorrect_guesses))
                                print('You did not enter nothin. Make sure its a letter from the alphabet and not a number, I am not making you guess Elon Musks kids name')
                        elif guess in letters_guessed:
                                print(draw_hangman(incorrect_guesses))
                                print('You already guessed that letter, try again!')
                        #Detuct tries each time user fails to guess incorrectly
                        elif guess not in word:
                                letters_guessed.append(guess)
                                tries-=1
                                print(draw_hangman(incorrect_guesses))
                                print('WHOOPS! Sorry, that letter is not part of the word : (')
                        elif guess in word:
                                print('YEP! That letter exists in the word!')
                                print(draw_hangman(incorrect_guesses))
                                letters_guessed.append(guess)
                        else:
                                print(draw_hangman(incorrect_guesses))
                                print('CHECK YOUR ENTRY! IT BETTER NOT BE A DIGIT >:(')
        #user inputs the full word
                elif len(guess) == len(word):
                        if guess == word:
                                print(draw_hangman(incorrect_guesses))
                                print('YAY! You got it!')
                                guessed = True
                        else:
                                tries-=1
                                print(draw_hangman(incorrect_guesses))
                                print('Sorry, that was not the word we were looking for :(')
        #user inputs letters and it is not equal to the total numebr of letters in the word to guess.
                else:
                        tries-=1
                        print(draw_hangman(incorrect_guesses))
                        print('The length of your guess is not the same as the length of the correct word.')

                status = ''
                if guessed == False:
                        for letter in word:
                                if letter in letters_guessed:
                                        status += letter
                                else:
                                        status += '_'
                        print(status)

                if status == word:
                        guessed = True
                        print(draw_hangman(incorrect_guesses))
                        print('Great Job! You guessed the word correctly!')
                elif tries == 0:
                        print(draw_hangman(incorrect_guesses))
                        print("Yikes! You ran out of guesses and you couldn't guess the word. The word was", word_to_guess)

        #Initiate 'PLAY_AGAIN" funtion if the user wishes to continue, at the end of this funtion
        play_again()

#Full Program run
game_run()
        
    