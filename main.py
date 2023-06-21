#from art import logo
import random

def randomNumber():
  """This function generates a random number between 1 to 100."""
  number = random.randint(1, 101)
  return number

def livesDown(lives):
  """This function decreases the number of lives by 1 and returns the updated value."""
  lives -= 1
  return lives

#print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
SECRET_NUMBER = randomNumber()
game = True

if difficulty == "easy":
  lives = 10
else:
  lives = 5

while game and lives > 0:
  guess = int(input("Make a guess: "))
  lives = livesDown(lives)

  if guess == SECRET_NUMBER:
    game = False
    print("You've guessed it! YOU WIN!") 
  elif lives == 0:
    game = False
    print(f"You ran out of attempts, you lose! The number was {SECRET_NUMBER}")
    
  elif guess < SECRET_NUMBER:
    print("Your guess is low. Please try again.")
    print(f"You have {lives} attempts remaining to guess the number.")
  else:
    print("Your guess is high. Please try again.")
    print(f"You have {lives} attempts remaining to guess the number.")
import random

def randomNumber():
  """This function generates a random number between 1 to 100."""
  number = random.randint(1, 101)
  return number

def livesDown(lives):
  """This function decreases the number of lives by 1 and returns the updated value."""
  lives -= 1
  return lives

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
SECRET_NUMBER = randomNumber()
game = True

if difficulty == "easy":
  lives = 10
else:
  lives = 5

while game and lives > 0:
  guess = int(input("Make a guess: "))
  lives = livesDown(lives)

  if guess == SECRET_NUMBER:
    game = False
    print("You've guessed it! YOU WIN!") 
  elif lives == 0:
    game = False
    print(f"You ran out of attempts, you lose! The number was {SECRET_NUMBER}")
    
  elif guess < SECRET_NUMBER:
    print("Your guess is low. Please try again.")
    print(f"You have {lives} attempts remaining to guess the number.")
  else:
    print("Your guess is high. Please try again.")
    print(f"You have {lives} attempts remaining to guess the number.")
