import random
rand = random.randrange(1,10)
print(rand)

gameStatus = False
attempts = 5

print("\nGuess the number between 1 - 10. GO!")
while gameStatus == False and attempts > 0:
    x = int(input())
    if x == rand:
        print("\nCongrats !!!")
        gameStatus = True
    elif attempts == 0:
        attempts -= 1
        print("\nGame Over ...")
    else:
        print(f"\nTry Again - Attempts Left: {attempts}\n")
