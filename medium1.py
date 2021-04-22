import random

real_number = random.randint(1,100)
tries = 0

while(True):
    guess_number = int(input("Enter your guess: "))
    if guess_number == real_number:
        tries += 1
        print(f"You got {real_number} correct after {tries} tries!")
        break;

    if guess_number > real_number:
        tries += 1
        print("Nice try, but next time guess lower!")

    if guess_number < real_number:
        tries += 1
        print("Nice try, but next time guess higher!")
    
