import random
lower = int(input("Enter lower number here: "))
upper = int(input("Enter upper number here: "))
x = random.randrange(lower, upper)


while True:
    guess = int(input("Guess a number: "))

    if guess < x:
        print("Guess is too low")
    elif guess > x:
        print("Guess is too high")
    elif guess == x:
        print("Correct")
        break
    else:
        pass