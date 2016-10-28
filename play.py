import game

iteration = 10
numberWin = [0, 0]
numSteps = [[0 for i in range(iteration)] for i in range(0, 2)]
boardSize = 15

for i in range(0, iteration):
	newGame = game.Gomoku(boardSize)
	# print "start a new Gomoku game with board size %dx%d"%(boardSize, boardSize)

	baselinePolicy = game.BaselinePolicy()
	randomPolicy = game.RandomPolicy()
	while (newGame.isEnd() < 0):
		nextPlayer = newGame.nextPlayer
		if (nextPlayer == 1):
			action = baselinePolicy.getNextAction(newGame)
		else:
			action = randomPolicy.getNextAction(newGame)
		# print "player %d places on (%d, %d)"%(nextPlayer, action[0], action[1])
		newGame.updateBoard(action)
	losePlayer, totalStep0, totalStep1 = newGame.currentGame()
	winPlayer = 2 if losePlayer == 1 else 1
	totalStep = (totalStep0, totalStep1)
	if newGame.isEnd() != 0:
		numberWin[winPlayer-1] += 1
		numSteps[winPlayer-1][i] = totalStep[winPlayer-1]
print "player 1 wins %d times, the average number of steps to win is %f"%(numberWin[0], 1.0*sum(numSteps[0])/numberWin[0])
print "player 2 wins %d times, the average number of steps to win is %f"%(numberWin[1], 1.0*sum(numSteps[1])/numberWin[1])

	# if newGame.isEnd() == 0:
	# 	print "break even!"
	# else:
	# 	print "Game ends! player %d wins in %d steps"%(winPlayer, totalStep[winPlayer - 1])
	# for i in range(0, boardSize):
	# 	print newGame.chessBoard[i]

