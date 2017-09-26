"""Israel Felhandler"""
"""IF12B"""
"""CIS4930 - Python"""
"""Summer 2017"""

from random import randint
from copy import deepcopy
import enchant
d = enchant.Dict("en_US")

#The 16 Dice with each face represented as a list of lists
myList = [['A','E','A','N','E','G'], ['A','H','S','P','C','O'], 
		['A','S','P','F','F','K'], ['O','B','J','O','A','B'],
		['I','O','T','M','U','C'], ['R','Y','V','D','E','L'],
		['L','R','E','I','X','D'], ['E','I','U','N','E','S'],
		['W','N','G','E','E','H'], ['L','N','H','N','R','Z'],
		['T','S','T','I','Y','D'], ['O','W','T','O','A','T'],
		['E','R','T','T','Y','L'], ['T','O','E','S','S','I'],
		['T','E','R','W','H','V'], ['N','U','I','M','Qu']]

#Randomly select one of the facesof each dice
myBoard = [[myList[0][randint(0,2)], myList[1][randint(0,2)],
myList[2][randint(0,2)], myList[3][randint(0,2)]], [myList[4][randint(0,2)],
myList[5][randint(0,2)], myList[6][randint(0,2)], myList[7][randint(0,2)]],
[myList[8][randint(0,2)], myList[9][randint(0,2)], myList[10][randint(0,2)],
myList[11][randint(0,2)]], [myList[12][randint(0,2)], myList[13][randint(0,2)],
myList[14][randint(0,2)], myList[15][randint(0,2)]]]

#Print the board
print("[%s] [%s] [%s] [%s]\n" %(myBoard[0][0], myBoard[0][1], myBoard[0][2], myBoard[0][3]))
print("[%s] [%s] [%s] [%s]\n" %(myBoard[1][0], myBoard[1][1], myBoard[1][2], myBoard[1][3]))
print("[%s] [%s] [%s] [%s]\n" %(myBoard[2][0], myBoard[2][1], myBoard[2][2], myBoard[2][3]))
print("[%s] [%s] [%s] [%s]\n" %(myBoard[3][0], myBoard[3][1], myBoard[3][2], myBoard[3][3]))
print("Start typing your words! (press enter after each word and enter 'X' when done):")

#Create list of the words entered by the user
listOfWords = []
while True:
    temp = raw_input()
    temp = temp.upper()
    if (temp == 'X'):
        break
    else:
        listOfWords.append(temp)

#Function to determine the points
def scoring(word, totalPts):
    if (len(word) < 5):
        pts = 1
    elif (len(word)) == 5:
        pts = 2
    elif (len(word)) == 6:
        pts = 3
    elif (len(word)) == 7:
        pts = 5
    else:
        pts = 11

    if (pts == 1):
        print "The word %s is worth 1 point." %(word)
        totalPts += pts
    else:
        print "The word %s is worth %d points." %(word, pts)
        totalPts += pts
    return totalPts

#Recursive function to check each letter of word
def checkLetter(board, word, letterPos, row, col):
    tempBoard = deepcopy(board)
    while (letterPos < len(word)):
        tempBoard[row][col] = '\0'
        if ((word[letterPos] == tempBoard[row-1][col-1]) and (row-1>=0) and (col-1>=0)):
            letterPos+=1
            checkLetter(tempBoard, word, letterPos, row-1, col-1)
        elif ((word[letterPos] == tempBoard[row-1][col]) and (row-1>=0)):
            letterPos+=1
            checkLetter(tempBoard, word, letterPos, row-1, col)
        elif ((word[letterPos] == tempBoard[row-1][col+1]) and (row-1>=0) and (col+1<=3)):
            letterPos+=1
            checkLetter(tempBoard, word, letterPos, row-1, col+1)
        elif ((word[letterPos] == tempBoard[row][col-1]) and (col-1>=0)):
            letterPos+=1
            checkLetter(tempBoard, word, letterPos, row, col-1)
        elif ((word[letterPos] == tempBoard[row][col+1]) and (col+1<=3)):
            letterPos+=1
            checkLetter(tempBoard, word, letterPos, row, col+1)
        elif ((word[letterPos] == tempBoard[row+1][col-1]) and (row+1<=3) and (col-1>=0)):
            letterPos+=1
            checkLetter(tempBoard, word, letterPos, row+1, col-1)
        elif ((word[letterPos] == tempBoard[row+1][col]) and (row+1<=3)):
            letterPos+=1
            checkLetter(tempBoard, word, letterPos, row+1, col)
        elif ((word[letterPos] == tempBoard[row+1][col+1]) and (row+1<=3) and (col+1<=3)):
            letterPos+=1
            checkLetter(tempBoard, word, letterPos, row+1, col+1)
        else:
            return 0

#Function to check word
def checkWord(word, board):
    check = False
    copy = deepcopy(board)
    letter = word[0:1]
    for i in range(0,4):
    	if (check == True):
    		break
        for j in range(0,4):
            if (check == True):
	            break
            elif (letter == copy[i][j]):
                nextCheck = [i, j]
                check = True
                x = checkLetter(copy, word, 1, i, j)
                if (x == 0):
                    check == False
                    break
    if (check != True):
        print "The word %s is not present." %(word)
    #else:
     #   for i in range(1,len(word))
    #print board    

	    #pop out
	    #
    else:
        return 

#Iterate through list of words and evaluate them
totalPts = 0
numWords = len(listOfWords)
for i in range(0,numWords):
    word = listOfWords[i]
    if (len(word) < 3):
        print "The word %s is too short." %(word)
    elif (d.check(word) == True):
        checkWord(word, myBoard)
        totalPts = scoring(word, totalPts)
    else:
        print "The word %s is ... not a word." %(word)
print "Your total score is %d points!" %(totalPts)