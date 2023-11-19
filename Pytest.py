import pytest
from slide_puzzle import *

class TestSlidePuzzle:
   def test_getStartingBoard(self):
       board = getStartingBoard()
       assert len(board) == BOARDWIDTH
       assert len(board[0]) == BOARDHEIGHT
       assert board[BOARDWIDTH-1][BOARDHEIGHT-1] == BLANK

   def test_isValidMove(self):
       board = getStartingBoard()
       assert isValidMove(board, UP) == False
       assert isValidMove(board, DOWN) == True
       assert isValidMove(board, LEFT) == False
       assert isValidMove(board, RIGHT) == True

   def test_makeMove(self):
      board = getStartingBoard()
      blankx, blanky = getBlankPosition(board)
      old_value = board[blankx][blanky]
      makeMove(board, UP)
      assert board[blankx][blanky] == old_value


   def test_getRandomMove(self):
       board = getStartingBoard()
       move = getRandomMove(board)
       assert move in [UP, DOWN, LEFT, RIGHT]

   

if __name__ == "__main__":
   pytest.main([__file__])
