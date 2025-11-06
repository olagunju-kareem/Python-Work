#! python3
# ticTacToe.py - A program that models the classic Tic Tac Toe game.

 
"""INSTRUCTIONS:
	* The board format is as shown below:
		1|2|3
		-+-+-
		4|5|6
		-+-+-
		7|8|9
		Enter the number that's in the position you want to play in."""
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
	while True:
		pos = input(prompt)
		if pos.isdecimal():
			x = int(pos)
			if x in range(1, 10):
				return x
			else:
				print('Please enter a number between 1 and 9.')
		else:
			print('Invalid Input!')
		

def printGame(board):
	print(f'{board[1]}|{board[2]}|{board[3]}'.rjust(5))
	print('-+-+-'.rjust(5))
	print(f'{board[4]}|{board[5]}|{board[6]}'.rjust(5))
	print('-+-+-'.rjust(5))
	print(f'{board[7]}|{board[8]}|{board[9]}'.rjust(5))
	
def main():
	board = BOARD.copy()
	turn = 'X'
	printGame(board)
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
		
		if board[1] == board[2] == board[3] != ' ':
			printGame(board)
			print(f'Player {board[1]} wins.')
			break
		elif board[4] == board[5] == board[6] != ' ':
			printGame(board)
			print(f'Player {board[4]} wins.')
			break
		elif board[7] == board[8] == board[9] != ' ':
			printGame(board)
			print(f'Player {board[7]} wins.')
			break
		elif board[1] == board[4] == board[7] != ' ':
			printGame(board)
			print(f'Player {board[1]} wins.')
			break
		elif board[2] == board[5] == board[8] != ' ':
			printGame(board)
			print(f'Player {board[2]} wins.')
			break
		elif board[3] == board[6] == board[9] != ' ':
			printGame(board)
			print(f'Player {board[3]} wins.')
			break
		elif board[3] == board[5] == board[7] != ' ':
			printGame(board)
			print(f'Player {board[3]} wins.')
			break
		elif board[1] == board[5] == board[9] != ' ':
			printGame(board)
			print(f'Player {board[1]} wins.')
			break
	else:
		print('\n')
		printGame(board)
		print("It's a tie.")

main()