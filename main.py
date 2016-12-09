from Evaluator import *
from FileIO import *
from AlphaBeta import *
from BoardLogic import *

alpha = float('-inf')
beta = float('inf')
depth = 3

def printBoard(board):
		
		print(board[0]+"(00)----------------------"+board[1]+"(01)----------------------"+board[2]+"(02)");
		print("|                           |                           |");
		print("|       "+board[8]+"(08)--------------"+board[9]+"(09)--------------"+board[10]+"(10)     |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       |        "+board[16]+"(16)-----"+board[17]+"(17)-----"+board[18]+"(18)       |      |");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print(board[3]+"(03)---"+board[11]+"(11)----"+board[19]+"(19)               "+board[20]+"(20)----"+board[12]+"(12)---"+board[4]+"(04)");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print("|       |        "+board[21]+"(21)-----"+board[22]+"(22)-----"+board[23]+"(23)       |      |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       "+board[13]+"(13)--------------"+board[14]+"(14)--------------"+board[15]+"(15)     |");
		print("|                           |                           |");
		print("|                           |                           |");
		print(board[5]+"(05)----------------------"+board[6]+"(06)----------------------"+board[7]+"(07)");
	



if __name__ == "__main__":
	

	board = []
	for i in range(24):
		board.append("X")

	evaluation = evaluator(board)
		
	
	for i in range(9):

		printBoard(board)
		placePiece(board)

		if getEvaluationForOpeningPhase(board) == 100000:
			print("Winner!")
			exit(0)
		
		printBoard(board)
		evalBoard = alphaBetaPruning(board, depth, False, alpha, beta, True)
		print(evalBoard.board)
		if evalBoard.evaluator == -100000:
			print("You Lost")
			exit(0)
		else:
			board = evalBoard.board

	while True:

		printBoard(board)
		movePiece(board)

		if getEvaluationForMidGameAndEndGame(board) == 100000:
			print("You Win!")
			exit(0)

		printBoard(board)

		evaluation = alphaBetaPruning(board, depth, False, alpha, beta, False)

		if evaluation.evaluator == -100000:
			print("You Lost")
			exit(0)
		else:
			board = evaluation.board















	
