for i in (1,2,3,4,5,6,7,8,9,10):
    if i == 3 : continue
guesses_left = 2
i = (int(input("Guess the number between 1 and 10\n")))
while guesses_left > 0:
    if i != 3 :
        print("guesses left=", guesses_left, end="")
        print()
        i = (int(input("Guess the number between 1 and 10\n")))
        guesses_left -= 1
    elif i == 3:
        print("you win", end="")
        exit()
else : guesses_left > 0
print("you lose",end="")
print()