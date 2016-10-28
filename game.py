from random import randint

class Gomoku:

	def __init__(self, N):
		# chess board
		self.chessBoard = [[0 for i in range(N)] for i in range(N)]
		self.chessSize = N

		# player 
		self.nextPlayer = 1
		self.lastMove 	= (-1, -1)
		self.totalSteps = [0, 0] # (player 1, player 2)

	def currentGame(self): # return the next player, total steps for player 1 and 2 respectively
		return (self.nextPlayer, self.totalSteps[0], self.totalSteps[1])

	# update chess board given a move
	def updateBoard(self, pos):
		assert(pos[0] >= 0 and pos[0] < self.chessSize and pos[1] >= 0 and pos[1] < self.chessSize)
		self.chessBoard[pos[0]][pos[1]] = self.nextPlayer
		self.totalSteps[self.nextPlayer - 1] += 1
		self.lastMove = pos
		self.nextPlayer = 2 if self.nextPlayer == 1 else 1

	# check if the game ends
	# return if a game terminates
		# -1 - not end
		# 0 - break even
		# 1 - player 1 wins
		# 2 - player 2 wins
	def isEnd(self): 

		# helper function to return state of a position
		def boardState(pos): # pos = (coor x, coor y)
			if (pos[0] < 0 or pos[0] >= self.chessSize or pos[1] < 0 or pos[1] >= self.chessSize):
				return -1
			else:
				return self.chessBoard[pos[0]][pos[1]]

		if sum(self.totalSteps) >= self.chessSize*self.chessSize:
			return 0
		direction = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1),
					'NE': (-1, 1), 'NW': (-1, -1), 'SE': (1, 1), 'SW': (1, -1)}
		count = {'N': 0, 'S': 0, 'W': 0, 'E': 0,
				'NE': 0, 'NW': 0, 'SE': 0, 'SW': 0}
		lastPlayer = 2 if self.nextPlayer == 1 else 1
		for d in direction:
			i = self.lastMove[0]
			j = self.lastMove[1]
			while boardState((i, j)) == lastPlayer:
				count[d] += 1
				i += direction[d][0]
				j += direction[d][1]
		# print count
		if (count['N'] + count['S'] >= 6) or (count['W'] + count['E'] >= 6) \
			or (count['NE'] + count['SW'] >= 6) or (count['NW'] + count['NE'] >= 6):
			return lastPlayer
		else:
			return -1

# a random policy 
class RandomPolicy:

	def getNextAction(self, game):
		agent = game.nextPlayer
		op = 2 if agent == 1 else 1
		chessBoard = game.chessBoard
		while True:
			x = randint(0,len(chessBoard) - 1)
			y = randint(0,len(chessBoard) - 1)
			if (chessBoard[x][y] == 0):
				return (x, y)

# a naive policy to play Gomoku
class BaselinePolicy:

	def getNextAction(self, game):
		agent = game.nextPlayer
		op = 2 if agent == 1 else 1
		chessBoard = game.chessBoard
		totalCount = 0
		nextMove = []

		# desired pattern
		fourInRow = ([op, op, op, op, 0], [0, op, op, op, op])
		threeInRow = ([0, op, op, op, 0], [agent, op, op, op, 0], [0, op, op, op, agent])
		for i in range(len(chessBoard)):
			for j in range(len(chessBoard)):
				allPattern = ( [chessBoard[p][j] if p >= 0 and p < len(chessBoard) else -2 for p in range(i-4, i+1)], \
								[chessBoard[p][j] if p >= 0 and p < len(chessBoard) else -2 for p in range(i, i+5)], \
								[chessBoard[i][p] if p >= 0 and p < len(chessBoard) else -2 for p in range(j-4, j+1)], \
								[chessBoard[i][p] if p >= 0 and p < len(chessBoard) else -2 for p in range(j, j+5)], \
								[chessBoard[i+p][j+p] if i + p >= 0 and i + p < len(chessBoard) and j + p >= 0 and j + p < len(chessBoard) else -2 for p in range(-4, 0)], \
								[chessBoard[i+p][j+p] if i + p >= 0 and i + p < len(chessBoard) and j + p >= 0 and j + p < len(chessBoard) else -2 for p in range(0, 5)] \
							)
				for pattern in allPattern:
					if (pattern in fourInRow and chessBoard[i][j] == 0):
						nextMove = [(i, j)] + nextMove
					elif (pattern in threeInRow and chessBoard[i][j] == 0):
						nextMove.append((i, j))
		# generate random position
		if len(nextMove) < 1:
			while True:
				x = randint(0,len(chessBoard) - 1)
				y = randint(0,len(chessBoard) - 1)
				if (chessBoard[x][y] == 0):
					nextMove.append((x, y))
					break
		return nextMove[0]







