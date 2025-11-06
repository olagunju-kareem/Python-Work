#! python3
# ticTacToe.py - A program that models the classic Tic Tac Toe game.
 
"""INSTRUCTIONS:
	The board format is as shown below:
		1|2|3
		-+-+-
		4|5|6
		-+-+-
		7|8|9
		Enter the number that's in the position you want to play in.
		I hope you have fun playing."""

BOARD = {
	1: ' ', 
	2: ' ', 
	3: ' ',
	4: ' ',
	5: ' ',
	6: ' ',
	7: ' ',
	8: ' ',
	9: ' ',
}

def inputPos(prompt):
	"""Ensures player inputs a valid position."""
	while True:
		pos = input(prompt)
		if pos.isdecimal():
			x = int(pos)
			if 1 <= x <= 9:
				return x
			else:
				print('Please enter a number between 1 and 9.')
		else:
			print('Invalid Input! Enter a number.')

def winGame(board):
	"""Helps to check for game win conditions."""
	winPositions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
		            (2, 5, 8), (3, 6, 9), (3, 5, 7), (1, 5, 9)]
	for positions in winPositions:
		if board[positions[0]] == board[positions[1]] == board[positions[2]] != ' ':
			return board[positions[0]]
	return None
		
def printGame(board):
	"""Prints game board."""
	print(f'{board[1]}|{board[2]}|{board[3]}')
	print('-+-+-')
	print(f'{board[4]}|{board[5]}|{board[6]}')
	print('-+-+-')
	print(f'{board[7]}|{board[8]}|{board[9]}')

def playAgain():
	"""Asks if user wants to play again."""
	while True:
		again = input('Would you like to play again? (y/n) ')
		if again in ['y', 'n']:
			if again == 'y':
				print('Welcome to another round of Tic Tac Toe.\n')
				return True
			else:
				print('It was nice having you, byeeee.')
				return False

	
def main():
	"""Main game."""
	board = BOARD.copy()
	turn = 'X'
	x_score = 0
	o_score = 0
	# Display score board.
	print(f'Player X: {x_score}     Player O: {o_score}')
	# Display board for players:
	printGame(board)
	# Ensure game continues given that empty spaces remain.
	while ' ' in board.values():
		while True:
			if turn == 'X':
				x_pos = inputPos('\nX turn: ')
				if board[x_pos] == ' ':
					board[x_pos] = 'X'
					turn = 'O'
					printGame(board)
					break
				else:
					print('Position already occupied! Try another position.')
			elif turn == 'O':
				o_pos = inputPos('\n0 turn: ')
				if board[o_pos] == ' ':
					board[o_pos] = 'O'
					turn = 'X'
					printGame(board)
					break
				else:
					print('Position already occupied! Try another position.')
		
		# Check for win, and then prompt player for another round or not
		win = winGame(board)
		if win:
			print(f'\nPlayer {win} wins.')
			if win == 'X':
				x_score += 1
			else:
				o_score += 1
			print(f'Player X: {x_score}     Player O: {o_score}')
			Again = playAgain()
			if Again:
				main()
			else:
				break

	# If no more empty spaces and no win, then game is a tie.
	else:
		print('\n')
		printGame(board)
		print("It's a tie.")
		Again = playAgain()
		if Again:
			main()

main()