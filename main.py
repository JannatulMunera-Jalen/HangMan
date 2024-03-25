#importing random module
import random

def welcome():
    while True:
        # Prompt the user to enter their name
        name = input("Welcome to Hangman Game!! Please enter your name, or not, I ain't your mama: ")

        # Check if a valid name is entered
        if name.isalpha():
            print("AYEEEE!", name, "My Mannn!! or woman, or a unicorn etc. <<< Rules simple. Computer picks a random word and you guess it. Easy right? So have fun! OH! and you only get 5 chances to guess else you're the reason why an innocent man gets hanged right in front of you! So, have fun! >>>")
            break  # Exit the loop if a valid name is entered
        else:
            print("Mate... You ain't got no option, type yo name.")

#Define another function PLAY_AGAIN
#Add a doctring
def play_again():

        """This function asks user/player if they wish to replay the game"""
        response = input("Would you like to play again? Enter 'Y' for yes, 'N' for No").lower()

        #Create a decision making process
        if response == 'y':
                game_run()
        else:
                print('You snoooooze, you looooose, see yah')

#Define another function GET_WORD for generating random words for the user to guess
#Add a docstring
def get_word():
        """This function generates the word the user will attempt guessing"""
        words = ['python','cool','battery','urban','meow']
        return random.choice(words).lower()       

#Define another function GAME_RUN(), add docstring if required
def game_run():
        """This function runs the game when invoked and basically call all the other functions that involves to be able to play this game"""
        
        #Call the 'WELCOME" function here to get the game running
        welcome()
        
        #Define an 'ALPHABET' variable
        alphabet = ('abcdefjhijklmnopqrstuvwxyz')
        
        #Set guess word to get_word fnction for a random word to be generated
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
                                print('You did not enter nothin. Make sure its a letter from the alphabet and not a number, I am not making you guess Elon Musks kids name')
                        elif guess in letters_guessed:
                                print('You already guessed that letter, try again!')
                        #Detuct tries each time user fails to guess incorrectly
                        elif guess not in word:
                                print('WHOOPS! Sorry, that letter is not part of the word : (')
                                letters_guessed.append(guess)
                                tries-=1
                        elif guess in word:
                                print('YEP! That leter exists in the word!')
                                letters_guessed.append(guess)
                        else:
                                print('CHECK YOUR ENTRY! IT BETTER NOT BE A DIGIT >:(')
        #user inputs the full word
                elif len(guess) == len(word):
                        if guess == word:
                                print('YAY! You got it!')
                                guessed = True
                        else:
                                print('Sorry, that was not the word we were looking for :(')
                                tries-=1
        #user inputs letters and it is not equal to the total numebr of letters in the word to guess.
                else:
                        print('The length of your guess is ot the same as the length of the correct word.')
                        tries-=1

                status = ''
                if guessed == False:
                        for letter in word:
                                if letter in letters_guessed:
                                        status += letter
                                else:
                                        status += '_'
                        print(status)

                if status == word:
                        print('Great Job! You guessed the word correctly!')
                        guessed = True
                elif tries == 0:
                        print("Yikes! You ran out of guesses and you couldn't guess the word.")

        #Initiate 'PLAY_AGAIN" funtion if the user wishes to continue, at the end of this funtion
        play_again()

#Full Program run
game_run()
        
    