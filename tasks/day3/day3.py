#number guessing program
import random

secret_number = random.randint(1, 10)  # Random number between 1 and 10

run = True

print("Guess the number between 1 and 10!")

def start():
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break  # Exit the loop

while(run):
    start()
    ch = int(input("You are continue the game!\nYes(1) or No(0):"))
    if(ch==1):
        pass
    else:
        run = False
        print("Bye bye...")
