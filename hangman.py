#! python3
# hangman.py - A program that models the classic hangman game. 

import random, time, pyinputplus as pyip
from string import ascii_letters

MAX_LIVES = 7
WORDS = ['banana', 'uranium', 'upgrade', 'salmonella', 'caviar', 'beautiful', 'engineer', 'malevolent', 'kitchen', 'domestic', 'physics', 'spanish', 'intense', 'trouser', 'hangman', 'python', 'aeroplane', 'android', 'university', 'electricity', 'pillow', 'anaconda', 'jaguar']

# Custom function to ensure one letter input:
def oneLetter():
	while True:
		user_input = input('\nGuess a letter: ')
		if len(user_input) == 1 and user_input in ascii_letters:
			return user_input.lower()
		else:
			print('Invalid input! Please, enter a single letter.')
			
# Main game loop
def main():
	while True:
		# Number of wrong guesses allowed till loss:
		lives = MAX_LIVES
	
		print('Welcome to the classic Hangman game by Kareem 🎉')
	
		# Randomly select a  word from words list
		game_word = random.choice(WORDS)
	
		# Print game representation of game wordp
		print(f"Word to guess: {' '.join('_' * len(game_word))}")
	
		# Make a list to store correct guesses, and underscores to represent unguessed letters
		c_guess = ['_' for i in range(len(game_word))]
		# List to store all guesses:
		guesses = []
	
		# Create loop to keep getting user input
		while True:
			# Get guess letter through the custom function and add to guesses list
			guess_letter = oneLetter()
		
			# If guess is correct and has not been guessed before, add guesses word to correct guesses and print.
			if (guess_letter in game_word) and (guess_letter not in c_guess):
				print('Yay! You guessed right.')
				for i, letter in enumerate(game_word):
					if letter == guess_letter:
						c_guess[i] = guess_letter
				print(' '.join(c_guess))
		
			# If guess is correct but has already been guessed.
			elif (guess_letter in guesses):
				print('You have already guessed this letter. Please,try another letter.')
		
			# If guess is wrong, deduct lives.
			else:
				lives -= 1
				if lives != 0:	
					print('Incorrect guess, try again!')
					print(f'You have {lives} lives left.')
					print(' '.join(c_guess))
				else:
					print('Game Over, you have exhausted your lives.')
					print(f'The correct word is "{game_word}".')
					break
		
			# If all the '_' have been replaced i.e all letters correctly guessed, end game.
			if '_' not in c_guess:
				print('\nCongratulations, you finished the game!')
				time.sleep(1)
				print('Take this ₦10 make you use am hold body 😂.')
				time.sleep(1)
				print('₦10')
				break
			guesses.append(guess_letter)
		
		again = pyip.inputYesNo('Would you like to play again?\n')
		if again == 'yes':
			print('\nYAY!')
			continue
		else:
			print('\nByeee,it seems you don\'t  want my ₦10 again 🌚.')
			break
			
main()	