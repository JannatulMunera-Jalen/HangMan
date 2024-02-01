#importing random module
import random

#define welcome function
def welcome():

        #define a name variable
        name = input(" Welcome to Hangman Game!! Please Enter your name, or not I aint your mama: ")

        #Case to accept only string as name
        if name.isalpha() == True:
                print(" AYEEEE!", name, " My Mannn!! or woman, or a unicorn etc. <<< Rules simple. Computer picks a random word and you guess it. Easy right? So have fun! OH! and you only get 5 chances to guess else you the reason why an innocent man get hanged right in front of you! soooo, have fun!>>>")

        else:
                print("Mate... You aint got option, type yo name.")
                name = input("Enter name: ")
                print(" AYEEEE!", name, " My Mannn!! or woman, or a unicorn etc. <<< Rules simple. Computer picks a random word and you guess it. Easy right? So have fun! OH! and you only get 5 chances to guess else you the reason why an innocent man get hanged right in front of you! soooo, have fun!>>>")

                