from random import *

def main():
	num = randrange(1, 100)

	user = raw_input('Enter a number (1-100): ')
	user = int(user)

	while user != num:
		if user > num:
			user = raw_input('Too high! Try again: ')
			user = int(user)
		else:
			user = raw_input('Too low! Try again: ')
			user = int(user)

	print 'You win! Go you!'
	
if __name__ == '__main__':
	main()