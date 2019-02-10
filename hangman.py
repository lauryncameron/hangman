'''
OBJECTIVE:
    The objective is to create a hangman game
ALGORITHM:
    First we need to write the three functions in our program
    The first function that will be defined is the function that randomly selects a word from the text dictionary we will create.
    The second function defined is the function that takes an input from the user which will be each letter guessed
    The third function defined will be the one that will take the letters guessed correctly and turns it into a string
    In order for the first function to work we need to create a text file that the program can reference.
    Next we need to make sure we are working in the main module
    No we need to create the various variables we are going to use to store the data the user enters.
    We need a variable for the word the computer picks.
    We will also need to create a set of data that holds the letters guessed wrong and another one for letters guessed correctly.
    Next we need to display an introduction to the program so users will know what to do.
    Next we will build a repetitive system, so that the user will keep guessing words 
    Next we will code the game itself
    The first step is to have the user guess a word.
    Next we will create different options whether the user guessed correct or incorrect
    The next step is to print out the number of guesses that the user has left and what they currently have guessed  correctly in the word
    The final step is a conditional at the end that lets them know if they won or not
PSUEDOCODE:
    This is taking the algorithm we just wrote and adding what code we can use to complete each step
    First we need to write the three functions in our program
    We will use the define functions tool to create the functions
    The first function that will be defined is the function that randomly selects a word from the text dictionary we will create.
    We will use the open() function and the .readlines() functions to bring the text file into the program
    The second function defined is the function that takes an input from the user which will be each letter guessed
    We will use the input() function to bring the users input into the program
    The third function defined will be the one that will take the letters guessed correctly and turns it into a string
    We will use a list and loop to check which letters they guessed and put it in the order of the word
    Create a text file that the program can reference
    We will use LiClipse to create the text file
    Next we need to make sure we are working in the main module
    We will use a conditional statement to check if we a are working in the main module
    Then, create the various variables we are going to use to store the data the user enters.
    We need a variable for the for the word the computer picks.
    We will also need to create a list for letters guessed wrong and another list for letters guessed correctly.
    Next we need to create a loop that allows the user to keep guessing
    We will use a while loop to repeat the game
    Next we will code the game itself
    The first step is to have the user guess a word
    Next we will create different options whether the user guessed correct or incorrect
    The next step is to print out the number  of guesses that the user has left and what they currently have guessed correctly  in the word
    We will use the .format() fucntion format the print statement
    The final step is a conditional statement that will print if the user won or not
    
    @author: ITAUser
'''

'''
This function brings in a text file and returns a random word from it
'''
def pick_random_word():
    f = open("words.txt", 'r')
    words = f.readlines()
    index = random.randint(0, len(words) - 1)
    word = words[index].strip()
    return word
'''
Function takes input from user for the next letter
'''
def ask_user_for_next_letter():
    letter = input("Guess your letter: ")
    return letter.strip().upper()
'''
function will create a string of letters guessed correctly and underscores for letters not yet guessed
'''
def generate_word_string(word, letters_guessed):
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")
    return " ".join(output)
import random

'''
checks that the module we are using is currently the main module
'''
if __name__ == '__main__':
    WORD = pick_random_word()
    
    letters_to_guess = set(WORD)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    num_guesses = 0
    
    print("Welcome to Hangman!")
    
    '''
    calls the pick_random_word() function and assigns word to string variable WORD
    '''
    while (len(letters_to_guess) > 0) and num_guesses < 6:
    
        '''
        makes input from user equal to variable guess and set guess to lowercase version of self
        '''
        guess = ask_user_for_next_letter()
        guess = guess.lower()
        
        '''
        checks if user's guess was guessed already
        '''
        if guess in correct_letters_guessed or \
                guess in incorrect_letters_guessed:
            print("You already guessed that letter.")
            continue
        
        ''' checks if letter is in letters_to_guess'''
        if guess in letters_to_guess:
            letters_to_guess.remove(guess)
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            num_guesses += 1
        
        word_string = generate_word_string (WORD, correct_letters_guessed)
        print(word_string)
        print("You have {} guesses left".format(6 - num_guesses))
        
        ''' Conditional that lets user know if they won or not and what the word is'''
        if num_guesses < 6:
            print ("Congratulations! You correctly guessed the word")
        else:
            print("Sorry, you lose! Your word was {}".format(WORD))

