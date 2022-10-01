from art import * #allows ASCII art to be displayed
import sys, copy, random, animations

def upperCase(word):  #makes sure the word is in upper case
    return word.upper()


def findWord(): # selects a word from the 4700-word.txt file
    word_list = open("4700-words.txt", "r").readlines()
    random_number = random.randint(0, len(word_list))
    word = upperCase(word_list[random_number].rstrip())
    return word


def total_lives(word):
    wordLength = len(word)

    if wordLength > 5: # the longer the word the more chances they get
        total_lives = lives = 8 # hangman length
    else:
        total_lives = lives = 5 
    
    return total_lives


def setup(word):
    if word == None:
        return None
    
    else:
        guesses = []  #clears guesses after any previous hangman games
        wordWithFullUnderlines = '_' * len(word)  #makes original word with blanks
        wordInUnderlines = " ".join(list(wordWithFullUnderlines))  #makes original word with spaces inbetween

        wordListedInLetters = list(word)  #word displayed as a list

        wordLength = int(len(word))  #finds out how many letters word has

        print("The word has " + str(wordLength) + " letters!\n")

        total_lives_ = total_lives(word)

        print("You have a total of " + str(total_lives_) + " lives: " + "♥ " * total_lives_)  #displays lives
        print(" ")

        livesLost = 0  #directly realates to number of lives lost hearts

        return total_lives_, total_lives_, livesLost, wordInUnderlines, wordListedInLetters, wordLength, guesses


def wordBlanks(guess, totalLettersSuccessfullyGuessed, wordInUnderlines, wordListedInLetters):  #makes a list for the guessed letters
    guessedLettersFrequency = wordListedInLetters.count(guess)
    wordListedInLetters_temp = copy.deepcopy(wordListedInLetters)
    frequencyOfLetterInWord = 0 #will differ depending on letter. Starts at zero and is then searched for
    locations = []

    if guess in wordListedInLetters: #when guess is successful
        while frequencyOfLetterInWord < guessedLettersFrequency: #accounts for every instance of the letter, and does the loop that many times
            guessedLetterLocation = wordListedInLetters_temp.index(guess)  #finding the location of the 1st instance of the guessed letter
            wordListedInLetters_temp[guessedLetterLocation] = "*" #replacing the letter with a star so that it cant be found again
            totalLettersSuccessfullyGuessed += 1
            frequencyOfLetterInWord += 1
            locations.append(guessedLetterLocation)

        for i in range(len(locations)): # change the underlined word to include the newly guessed letters
            wordInUnderlines = wordInUnderlines[:locations[i]*2] + guess + wordInUnderlines[(locations[i]*2)+1:]

    return totalLettersSuccessfullyGuessed, wordInUnderlines, wordListedInLetters


def guessing(word, total_lives, lives, livesLost, wordInUnderlines, wordListedInLetters, wordLength, guesses, totalLettersSuccessfullyGuessed):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print(wordInUnderlines)  #prints new word with letters added to the blanks
    print("")

    if lives == 0:  #with no lives
        animations.hangmanAnimation_5(0)
        print("You lost! The word was '" + word + "'.\n")
        return Complete

    elif totalLettersSuccessfullyGuessed == wordLength:
        print("")
        if lives == 1:
            print("Congrats on guessing the word '" + ("").join(wordListedInLetters) + "' with just  " + "♥  life left!\n")
        else:
            print("Congrats on guessing the word '" + ("").join(wordListedInLetters) + "' with  " + "♥ " * lives + " lives left!\n")
        return Complete


    if len(guesses) >= 1:
        print("Guessed Letters: " + str(guesses) + "\n")  #tells the letters that have been guessed
    
    guess = input("Guess a letter: ").upper()  #Asks for user to guess letter
    print('')

    if str(guess) in guesses:  #sees if guess was already guessed
        print("You've already guessed that letter! \n")
        return word, total_lives, lives, livesLost, wordInUnderlines, wordListedInLetters, wordLength, guesses, totalLettersSuccessfullyGuessed

    elif len(guess) > 1:  #sees if guess is more than one letter
        print("That's not a letter! \n")
        return word, total_lives, lives, livesLost, wordInUnderlines, wordListedInLetters, wordLength, guesses, totalLettersSuccessfullyGuessed

    elif guess.lower() in letters:  
        guesses.append(guess)  #adds guess to guesses list

        if str(guess) in wordListedInLetters:  #when the guessed letter is in the word
            print("Well Done! You got a letter!")
            totalLettersSuccessfullyGuessed, wordInUnderlines, wordListedInLetters = wordBlanks(guess, totalLettersSuccessfullyGuessed, wordInUnderlines, wordListedInLetters)  #directs so that new format of the word can be printed (since the newly guessed letter)

        else:  #when guess is not in word
            livesLost = int(livesLost) + 1  #increases lives that are lost
            lives = lives - 1  #decreases lives
            print("Not in the word... Try Again!")

    else: 
        print("That's not a letter! \n")
        guessing()


    if lives == 1:
        print("You only have " + str(lives) + " life: " + "♥ " * lives + "♡ " * livesLost + "\n")

    else:
        print("You still have " + str(lives) + " lives: " + "♥ " * lives + "♡ " * livesLost + "\n")
    
    if total_lives == 5:
        animations.hangmanAnimation_5(lives) #directs to Hangman Animation
    else:
        animations.hangmanAnimation_8(lives)

    return word, total_lives, lives, livesLost, wordInUnderlines, wordListedInLetters, wordLength, guesses, totalLettersSuccessfullyGuessed 


def tryAgain():  #func that asks if the user wants to play again
    print("===============================================================\n")
    playAgain = input("Do you want to play again? If so type 'Y' ").lower()  #asks if they want to play again
    print("")
    if (playAgain == "y"):
        print("===============================================================")
        main()

    else:
        print("Oh well... See you next time!\n")
        sys.exit()


def main():  #starts code
    word = findWord()  #directs to func to pick a word
    total_lives, lives, livesLost, wordInUnderlines, wordListedInLetters, wordLength, guesses = setup(word)
    totalLettersSuccessfullyGuessed = 0

    while True:
        try:
            word, total_lives, lives, livesLost, wordInUnderlines, wordListedInLetters, wordLength, guesses, totalLettersSuccessfullyGuessed = guessing(word, total_lives, lives, livesLost, wordInUnderlines, wordListedInLetters, wordLength, guesses, totalLettersSuccessfullyGuessed)
        except:
            break

    tryAgain()  #directs to func to ask if user wants to play again


if __name__ == "__main__":
    print(" ")
    print("Welcome to...")
    tprint("HANGMAN","tarty1")
    animations.hangmanAnimation_5(0)

    main()
