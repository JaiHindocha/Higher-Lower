import random

print('Welcome to the higher or lower game.')
print('The computer will generate a number between 1 and 100')


number=random.randint(1,99)
numGuess=0
guesses=[]

while True:
	guess= int(input("Enter a number: "))
	while guess not in range(1,100):
		guess=int(input("Enter a number between 1 and 99: "))

	if guess > number:
		print('Lower')

	elif guess < number:
		print("Higher")

	else:
		break

	numGuess+=1
	guesses.append(guess)

print("It took you:",numGuess,'guesses.')
print("You guessed:",guesses)
print("The number was:",number)
