import time
import random
file =open("animals.txt","r")
picParts = ['  _____     ____', ' /      \  |  o | ', '|        |/ ___\|','|_________/     ','|_|_| |_|_|']
fullPic = """  _____     ____
 /      \  |  o | 
|        |/ ___\| 
|_________/     
|_|_| |_|_|"""
cont = True 
wordList = []
for i in file:
    wordList.append(i)
def getBoard(randomWord,letters):
    board = ''
    for i in randomWord:
        if i in letters:
            board += i
        else:
            board += '_'
        board += ' '
    return board       
def displayTurtle():
    if wrongCount > 0:
        for i in range(wrongCount):
            print(picParts[i])
        print('\nHERE IS YOUR TURTLE SO FAR')
    else:
        print("no turtle parts yet")
def intro():
    print("This is don't be turtle!")
    time.sleep(1.5)
    print("A game where you try not to be a turtle.")
    time.sleep(1.5)
    print("You know the guy.")
    time.sleep(1.5)
    print("""  _____     ____
 /      \  |  o | 
|        |/ ___\| 
|_________/     
|_|_| |_|_|""")
    time.sleep(1.5)
    print("This loser.")
    time.sleep(2.5)
    print("...OK so same rules as hangman except it's a turtle")
    print("But the word is picked from a list of 100 different animals")
    time.sleep(4)
    print("Good luck")

def getRandomWord():
    word = wordList[random.randint(0,len(wordList))]
    return word[0:-1]

while cont == True:
    wrongCount = 0
    letters = ''
    intro()
    randomWord = getRandomWord()
    board = '_'
    while wrongCount <= 5 and '_' in board:
        guess = input('Guess a letter')
        if guess not in randomWord:
            wrongCount += 1
            if 5 - wrongCount > 0:
                print('sorry not in there. you have ' + str(5 - wrongCount) + ' number of guesses left')
        elif guess in letters:
            print('you already got that one')
            continue
        else:
            letters += guess
        board = getBoard(randomWord, letters)
        print(board)
        displayTurtle()
    print("Oh wow what are the odds...guess you're a turtle anyway \n YOU LOSE!")     
    cont = input('If you want to play again, enter "y".')
    cont = cont.startswith("y")
file.close()