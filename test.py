##############################
## test cases for sanity check
##############################

import game, util

def SanityCheckEvaluationFunction():
	chessBoardSize = 6
	print "create a new chess board: "
	newGame = game.Gomoku(chessBoardSize)
	newGame.updateBoard((1,2)) # agent
	newGame.updateBoard((3,1)) # opp
	newGame.updateBoard((2,2)) # agent
	newGame.updateBoard((4,1)) # opp
	newGame.updateBoard((4,2)) # agent
	newGame.updateBoard((5,1)) # opp
	newGame.updateBoard((5,2)) # agent
	newGame.updateBoard((3,4)) # opp
	newGame.updateBoard((3,3)) # agent
	util.prettyPrint(newGame.chessBoard)
	value = game.evaluate(newGame, 1)
	assert(value == 17) # window count = {1: 6, 2: 2, 3: 1, 4: 1}
	print "pass test for evaluation function"

SanityCheckEvaluationFunction()