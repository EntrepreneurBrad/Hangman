import random  #importing code that allows for randomisation (selection of a word in the list)


def tryAgain():  #func that asks if the user wants to play again
    global word
    print("===============================================================")
    print(" ")
    playAgain = input("Do you want to play again? If so type 'r' ").lower(
    )  #asks if they want to play again
    if (playAgain == "r"):
        print("")
        print(
            "===============================================================")
        start()

    else:
        print(" ")
        print("Oh well... See you next time!")


def livesFunc():
    global lives, wordAsList, livesLost, wordSpaces

    lives = 5  #number of lives before death

    print("You have a total of " + str(lives) + " lives: " +
          "♥ " * lives)  #displays lives
    print(" ")

    livesLost = 0  #directly realates to number of lives lost hearts

    wordStateOriginal = '_' * len(word)  #makes original word with blanks
    wordAsList = list(wordStateOriginal)
    wordSpaces = " ".join(
        wordAsList)  #makes original word with spaces inbetween

    guessing()  #goes to the guessing func


def hangmanAnimation():
    global lives

    if lives == 5:  #with all 5 lives
        print(" ")
        print("     +------+")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print(" *************")
        print(" ")

    if lives == 4:  #with 4 lives
        print(" ")
        print("     +------+")
        print("     |      |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print(" *************")
        print(" ")

    if lives == 3:  #with 3 lives
        print(" ")
        print("     +------+")
        print("     |      |")
        print("     0      |")
        print("            |")
        print("            |")
        print("            |")
        print("            |")
        print(" *************")
        print(" ")

    if lives == 2:  #with 2 lives
        print(" ")
        print("     +------+")
        print("     |      |")
        print("     0      |")
        print("    \|/     |")
        print("            |")
        print("            |")
        print("            |")
        print(" *************")
        print(" ")

    if lives == 1:  #with 1 life
        print(" ")
        print("     +------+")
        print("     |      |")
        print("     0      |")
        print("    \|/     |")
        print("     |      |")
        print("            |")
        print("            |")
        print(" *************")
        print(" ")


def wordBlanks():
    global wordState, word, guess, guessedLettersIndex, wordLength, wordSpaces, totalLetterCounter, wordSpaces

    guessedLettersIndex = [
    ]  #makes a list for the index numbers of the guessed letters

    wordList = list(word)  #word displayed as a list

    letterCounter = 0

    if guess in wordList:
        index = wordList.index(
            guess)  #finding the 1st instance of guess letter
        guessedLettersIndex.append(index)
        wordSlice = slice((index + 1),
                          20)  #slicing word so that 2nd instance can be found
        wordList = wordList[wordSlice]
        letterCounter = letterCounter + 1

    if guess in wordList:
        index1 = wordList.index(
            guess)  #finding the 1st instance of guess letter
        indexAppending = index + 1 + index1  #makes an accurate index number beacuse when slicing it resets at 0
        guessedLettersIndex.append(
            indexAppending)  #adds letter num index to index
        wordSlice = slice((index1 + 1),
                          20)  #slicing word so that 2nd instance can be found
        wordList = wordList[wordSlice]  #actually slices word
        letterCounter = letterCounter + 1

    if guess in wordList:
        index2 = wordList.index(
            guess)  #finding the 1st instance of guess letter
        indexAppending = index + 1 + index1 + index2  #makes an accurate index number beacuse when slicing it resets at 0
        guessedLettersIndex.append(
            indexAppending)  #adds letter num index to index
        wordSlice = slice((index2 + 1),
                          20)  #slicing word so that 2nd instance can be found
        wordList = wordList[wordSlice]  #actually slices word
        letterCounter = letterCounter + 1

    if guess in wordList:
        index3 = wordList.index(
            guess)  #finding the 1st instance of guess letter
        indexAppending = index + 1 + index1 + index2 + index3  #makes an accurate index number beacuse when slicing it resets at 0
        guessedLettersIndex.append(
            indexAppending)  #adds letter num index to index
        wordSlice = slice((index3 + 1),
                          20)  #slicing word so that 2nd instance can be found
        wordList = wordList[wordSlice]  #actually slices word
        letterCounter = letterCounter + 1

    totalLetterCounter = letterCounter + totalLetterCounter

    if letterCounter > 0:
        letterCounter = letterCounter - 1
        letterIndex = guessedLettersIndex[0]
        guessedLettersIndex.remove(letterIndex)

        slicing = (letterIndex * 2)

        slicingWordFirst = slice(
            slicing)  #prepares to slice for prior to guess
        actuallySlicingWordFirst = wordSpaces[
            slicingWordFirst]  #actually slices prior to guess

        guessInsert = guess  #formats guess ready for insert

        slicingWordSecond = slice(slicing + 1,
                                  20)  #prepares to slice after guess
        actuallySlicingWordSecond = wordSpaces[
            slicingWordSecond]  #actually slicing after guess
        wordSpaces = str(actuallySlicingWordFirst) + str(guessInsert) + str(
            actuallySlicingWordSecond)  #combines all

    if letterCounter > 0:
        letterCounter = letterCounter - 1
        letterIndex = guessedLettersIndex[0]
        guessedLettersIndex.remove(letterIndex)

        slicing = (letterIndex * 2)

        slicingWordFirst = slice(
            slicing)  #prepares to slice for prior to guess
        actuallySlicingWordFirst = wordSpaces[
            slicingWordFirst]  #actually slices prior to guess

        guessInsert = guess  #formats guess ready for insert

        slicingWordSecond = slice(slicing + 1,
                                  20)  #prepares to slice after guess
        actuallySlicingWordSecond = wordSpaces[
            slicingWordSecond]  #actually slicing after guess
        wordSpaces = str(actuallySlicingWordFirst) + str(guessInsert) + str(
            actuallySlicingWordSecond)  #combines all

    if letterCounter > 0:
        letterCounter = letterCounter - 1
        letterIndex = guessedLettersIndex[0]
        guessedLettersIndex.remove(letterIndex)

        slicing = (letterIndex * 2)

        slicingWordFirst = slice(
            slicing)  #prepares to slice for prior to guess
        actuallySlicingWordFirst = wordSpaces[
            slicingWordFirst]  #actually slices prior to guess

        guessInsert = guess  #formats guess ready for insert

        slicingWordSecond = slice(slicing + 1,
                                  20)  #prepares to slice after guess
        actuallySlicingWordSecond = wordSpaces[
            slicingWordSecond]  #actually slicing after guess
        wordSpaces = str(actuallySlicingWordFirst) + str(guessInsert) + str(
            actuallySlicingWordSecond)  #combines all

    if letterCounter > 0:
        letterCounter = letterCounter - 1
        letterIndex = guessedLettersIndex[0]
        guessedLettersIndex.remove(letterIndex)

        slicing = (letterIndex * 2)

        slicingWordFirst = slice(
            slicing)  #prepares to slice for prior to guess
        actuallySlicingWordFirst = wordSpaces[
            slicingWordFirst]  #actually slices prior to guess

        guessInsert = guess  #formats guess ready for insert

        slicingWordSecond = slice(slicing + 1,
                                  20)  #prepares to slice after guess
        actuallySlicingWordSecond = wordSpaces[
            slicingWordSecond]  #actually slicing after guess
        wordSpaces = str(actuallySlicingWordFirst) + str(guessInsert) + str(
            actuallySlicingWordSecond)  #combines all


def guessing():
    global livesLost, lives, guesses, wordState, wordList, guess, wordLength, totalLetterCounter

    print(wordSpaces)  #prints new word with letters added to the blanks
    print(" ")

    if lives == 0:  #with no lives

        print(" ")
        print("     +------+")
        print("     |      |")
        print("     0      |")
        print("    \|/     |")
        print("     |      |")
        print("    / \     |")
        print("            |")
        print(" *************")

        print(" ")
        print("You lost! The word was '" + word + "'.")
        print("\n")

        tryAgain()  #takes to play again func

    if totalLetterCounter == wordLength:
        print(" ")
        if lives == 1:
            print("Congrats on guessing the word '" + word + "' with just  " +
                  "♥ " * lives + " life left!")
            print(" ")
        else:
            print("Congrats on guessing the word '" + word + "' with  " +
                  "♥ " * lives + " lives left!")
            print(" ")
        tryAgain()  #make a way to sense word is fully guessed

    if len(guesses) >= 1:
        print("Guessed Letters: " +
              str(guesses))  #tells the letters that have been guessed
        print(" ")

    print(" ")
    guess = input("Guess a letter: ").upper()  #Asks for user to guess letter
    print(' ')

    if str(guess) in guesses:  #sees if guess was already guessed
        print("You've already guessed that letter!")
        print(" ")
        guessing()

    guesses.append(guess)  #asks guess to guesses list

    if str(guess) in word:  #when the guessed letter is in the word
        print("Well Done! You got a letter!")
        if lives == 1:
            print("You only have " + str(lives) + " life: " + "♥ " * lives +
                  "♡ " * livesLost)
            print(" ")
        else:
            print("You still have " + str(lives) + " lives: " + "♥ " * lives +
                  "♡ " * livesLost)
            print(" ")

        wordBlanks()  #directs so that new format of letter can be printed
        hangmanAnimation()  #directs to Hangman Animation
        guessing()  #restarts guessing

    else:  #when guess is not in word
        livesLost = int(livesLost) + 1  #increases lives that are lost
        lives = lives - 1  #decreases lives
        print("Not in the word... Try Again!")
        if lives == 1:
            print("You only have " + str(lives) + " life: " + "♥ " * lives +
                  "♡ " * livesLost)
            print(" ")
        else:
            print("You still have " + str(lives) + " lives: " + "♥ " * lives +
                  "♡ " * livesLost)
            print(" ")
        print(" ")
        hangmanAnimation()  #directs to Hangman Animation
        guessing()  #restarts guessing


def findWord():
    global word, wordLength, totalLetterCounter

    totalLetterCounter = 0  #a counter to tell when the user guesses the word

    wordList = [
        'icy', 'grieving', 'disillusioned', 'futuristic', 'skin', 'verdant',
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
        'offensive', 'act', 'loss', 'girl', 'motionless', 'daydream', 'steady',
        'demonic'
    ]
    chooseWord = random.choice(wordList)  #chooses one of the words
    word = str(chooseWord).upper()  #puts word in UPPERCASE

    wordLength = int(len(word))  #finds out how many letters word has
    print(" ")
    print("The word has " + str(wordLength) + " letters")
    print(" ")

    livesFunc()  #directs to lives making function


print(" ")
print("Welcome to...")
print(" ")
print(
    " __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __. "
)
print(
    '|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  | '
)
print(
    '|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  | '
)
print(
    '|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  | '
)
print(
    '|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   | '
)
print(
    '|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__| '
)
print(" ")
print("     +------+  ")
print("     |      |  ")
print("     0      | ")
print("    \|/     | ")
print("     |      | ")
print("    / \     | ")
print("            | ")
print(" *************")


def start():  #starts code
    global guesses
    guesses = []  #clears guesses after any previous hangman games
    findWord()  #directs to func to pick a word


start()  #directs to first func
