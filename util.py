
def prettyPrint(board):
	chessSize = len(board)
	for i in range(chessSize):
		for j in range(chessSize):
			if board[i][j] == 1:
				print 'x |', 
			elif board[i][j] == 2:
				print 'o |',
			else:
				print '  |',
		print '\n'