import random

# Generate a random number between 1 and 9
target_num = random.randint(1, 9)

while True:
     #Prompt the user to input a guess
    guess_num = int(input("Guess a number between 1 and 9: "))
    
    if guess_num == target_num:
        print("Well guessed!")
        break
    else:
        print("Incorrect! Try again.\n")

