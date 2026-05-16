import random
print("=== NUMBER GUESSING GAME ===")
secret_number = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess > secret_number:
        print("Too High!")
    elif guess < secret_number:
        print("Too Low!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
