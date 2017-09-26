==================
      Boggle
==================

Made By: Israel Felhandler

This is a 1-player Boggle simulator. The 16-dice are "rolled" and randomly positioned on a 4x4 grid. The player types words that appear in the grid, pressing ENTER to seperate, and ends the game by typing X. A review of the words that were typed along with their respective scores is printed, followed by a final score.

Scoring:
Word length   Points
    3,4          1
     5           2
     6           3
     7           5
     8+         11

SAMPLE RUN:

>>> python boggle.py 
[S] [E] [T] [T]
[O] [A] [N] [T]
[M] [O] [V] [E] 
[T] [H] [E] [E] 

Start typing your words! (press enter after each word and enter 'X' when done): 
>>> TEN 
>>> OVEN 
>>> MOVE 
>>> MOVED 
>>> TEAM 
>>> TEA 
>>> AT 
>>> MATE 
>>> NAOS 
>>> TEA 
>>> X 
The word TEN is worth 1 point. 
The word OVEN is worth 1 point. 
The word MOVE is worth 1 point. 
The word MOVED is not present. 
The word TEAM is worth 1 point. 
The word TEA is worth 1 point. 
The word AT is too short. 
The word MATE is worth 1 point. 
The word NAOS is ... not a word. 
The word TEA has already been used.
Your total score is 6 points!
