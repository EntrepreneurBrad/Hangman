import random  #importing code that allows for randomisation (selection of a word in the list)

breakLine = "==============================================================="

def tryAgain():  #func that asks if the user wants to play again
    global word
    print(breakLine)
    print(" ")
    playAgain = input("Do you want to play again? If so type 'r' ").lower()  #asks if they want to play again
    if (playAgain == "r"):
        print("")
        print(breakLine)
        start()

    else:
        print(" ")
        print("Oh well... See you next time!")


def livesFunc():
    global lives, wordsLettersInList, livesLost, wordInUnderlines

    lives = 5  #number of lives before death

    print("You have a total of " + str(lives) + " lives: " + "♥ " * lives)  #displays lives
    print(" ")

    livesLost = 0  #directly realates to number of lives lost hearts

    wordWithFullUnderlines = '_' * len(word)  #makes original word with blanks
    wordsLettersInList = list(wordWithFullUnderlines)
    wordInUnderlines = " ".join(wordsLettersInList)  #makes original word with spaces inbetween

    guessing()  #goes to the guessing func


def hangmanAnimation():
    global lives

    if lives == 5:  #with all 5 lives
        print("""
   +------+
          |
          |
          |
          |
          |
          |
*************
        """)

    if lives == 4:  #with 4 lives
        print("""
   +------+
   |      |
          |
          |
          |
          |
          |
*************
        """)

    if lives == 3:  #with 3 lives
      print("""
   +------+
   |      |
   0      |
          |
          |
          |
          |
*************
        """)

    if lives == 2:  #with 2 lives
      print("""
   +------+
   |      |
   0      |
  \|/     |
          |
          |
          |
*************
        """)

    if lives == 1:  #with 1 life
        print("""
   +------+
   |      |
   0      |
  \|/     |
   |      |
          |
          |
*************
        """)



def wordBlanks():
    global word, guess, listForGuessedLetters, wordLength, totalLettersSuccessfullyGuessed, wordInUnderlines, wordListedInLetters

    listForGuessedLetters = []  #makes a list for the guessed letters

    numOfLettersSuccessfullyGuessed = 0

    guessedLettersFrequency = wordListedInLetters.count(guess)
    frequencyOfLetterInWord = 0 #will differ depending on letter. Starts at zero and is then searched for
    print("letter occurs: " + str(guessedLettersFrequency))
    trueLetterPosition = 0 #the offset that occurs when a letter is removed so that the next instance of it can be identified. It resets each new type of letter
 
    wordListedInLetters = list(word) #resets word format for a new letter type

    if guess in wordListedInLetters: #when guess is successful

        while frequencyOfLetterInWord < guessedLettersFrequency: #accounts for every instance of the letter, and does the loop that many times
            guessedLetterLocation = wordListedInLetters.index(guess)  #finding the location of the 1st instance of the guessed letter
            trueLetterPosition = frequencyOfLetterInWord + guessedLetterLocation #an offset that keeps the shift (due to the removal of the first instance/s of a letter)
            listForGuessedLetters.append(trueLetterPosition) #adds to the list for the guessed letters (to keep track so that a double up doesnt occur if the letter is guessed again)
            wordInLettersSlicedPrior = wordListedInLetters[slice(guessedLetterLocation)]
            wordInLettersSlicedAfter = wordListedInLetters[slice((guessedLetterLocation + 1), 30)]
            wordListedInLetters = wordInLettersSlicedPrior + wordInLettersSlicedAfter
            numOfLettersSuccessfullyGuessed += 1
            frequencyOfLetterInWord += 1
            
            lettersFirstInstancePosition = listForGuessedLetters[0] #fetching the first instance of the letter in the array listForGuessedLetters (which stores this)
            listForGuessedLetters.remove(lettersFirstInstancePosition) #removing the first instance of the letter in the listForGuessedLetters array
            actualPositionWithUnderlines = (lettersFirstInstancePosition * 2) #for the spacing, two digits worth of space is needed "_ R _" (spaces)
            wordInUnderlinesSlicedPrior = wordInUnderlines[slice(actualPositionWithUnderlines)] #begins to slice the list just before the underline that is now going to be showcased by a letter
            wordInUnderlinesSlicedAfter = wordInUnderlines[slice((actualPositionWithUnderlines + 1), 30)]  #slices the list just after the underline (set to be showcased by a letter)
            wordInUnderlines = str(wordInUnderlinesSlicedPrior) + str(guess) + str(wordInUnderlinesSlicedAfter) #makes final word ready to be printed

    totalLettersSuccessfullyGuessed = numOfLettersSuccessfullyGuessed + totalLettersSuccessfullyGuessed #keeps track of successfully guessed letters so that once all letters are guessed the game is done


def guessing():
    global livesLost, lives, guesses, guess, wordLength, totalLettersSuccessfullyGuessed

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    print(wordInUnderlines)  #prints new word with letters added to the blanks
    print(" ")

    if lives == 0:  #with no lives
        print("""
   +------+
   |      |
   0      |
  \|/     |
   |      |
  / \     |
          |
*************
        \n""")
        print("You lost! The word was '" + word + "'.\n")

        tryAgain()  #takes to play again func


    if totalLettersSuccessfullyGuessed == wordLength:
        print(" ")
        if lives == 1:
            print("Congrats on guessing the word '" + word + "' with just  " + "♥ " * lives + " life left!\n")
        else:
            print("Congrats on guessing the word '" + word + "' with  " + "♥ " * lives + " lives left!\n")
        tryAgain()  #the user can play another round using this func

    if len(guesses) >= 1:
        print("Guessed Letters: " + str(guesses) + "\n")  #tells the letters that have been guessed
    
    guess = input("Guess a letter: ").upper()  #Asks for user to guess letter
    print(' ')

    if str(guess) in guesses:  #sees if guess was already guessed
        print("You've already guessed that letter! \n")
        guessing()

    elif len(guess) > 1:  #sees if guess is more than one letter
        print("That's not a letter! \n")
        guessing()  

    elif guess.lower() in letters:  

        guesses.append(guess)  #adds guess to guesses list

        if str(guess) in word:  #when the guessed letter is in the word
            print("Well Done! You got a letter!")
            wordBlanks()  #directs so that new format of the word can be printed (since the newly guessed letter)

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
    
    hangmanAnimation()  #directs to Hangman Animation
    guessing()  #restarts guessing for another guess


def findWord():
    global word, wordLength, totalLettersSuccessfullyGuessed, wordListedInLetters

    totalLettersSuccessfullyGuessed = 0  #a counter to tell when the user guesses the word

    wordListedInLetters = [
        'icy', 'grieving', 'disillusioned', 'futuristic', 'skin',
        'explode', 'quilt', 'wide', 'irritate', 'kill', 'compare',
        'superficial', 'store', 'pocket', 'digestion', 'drum', 'absurd',
        'minister', 'winter', 'mean', 'ground', 'copper', 'rude', 'class',
        'abiding', 'bomb', 'wire', 'imagine', 'bike', 'maddening', 'giraffe',
        'stick', 'destruction', 'filthy', 'acid', 'capable', 'drop', 'skirt',
        'fanatical', 'peep', 'accurate', 'berry', 'channel', 'turn', 'scary',
        'amazing', 'money', 'beneficial', 'generousity', 'shoes', 'unsuitable',
        'keen', 'violent', 'sniff', 'button', 'separate', 'temperature',
        'bright', 'meeting', 'superior', 'tired', 'vast', 'marvelous',
        'concentration', 'argument', 'jumbled', 'sparkling', 'happening',
        'lamp', 'informative', 'sharpening', 'hurrying', 'dreamy', 'poisonous',
        'creator', 'corn', 'private', 'roasted', 'wood', 'weather', 'touch',
        'gun', 'quiver', 'spiritual', 'admiration', 'gold', 'afternoon',
        'offensive', 'act', 'loss', 'girl', 'motionless', 'daydream', 'steady'
        ]
    
    chooseWord = random.choice(wordListedInLetters)  #chooses one of the words
    word = str(chooseWord).upper()  #puts word in UPPERCASE
    wordListedInLetters = list(word)  #word displayed as a list

    wordLength = int(len(word))  #finds out how many letters word has
    print(" ")
    print("The word has " + str(wordLength) + " letters\n")

    livesFunc()  #directs to lives making function


print(" ")
print("Welcome to...\n")
print("""
 __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.
|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | 
|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | 
|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | 
|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | 
|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| 
\n""")
print("""
   +------+
   |      |
   0      |
  \|/     |
   |      |
  / \     |
          |
*************
\n""")


def start():  #starts code
    global guesses
    guesses = []  #clears guesses after any previous hangman games
    findWord()  #directs to func to pick a word


start()  #directs to first func
