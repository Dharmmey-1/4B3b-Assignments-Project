

#GUESSING GAME. 

# THE BEST APPROACH TO SOLVE THIS GUESSING GAME IS USING WHILE LOOP BEACUSE IT WILL ITERATE OVER THE LOOP WHEN A CONDITION IS TRUE AND STOP WHEN IT IS FALSE.

# HOWEVER, I HAVE TO CHECK WHAT TYPE OF WHILE LOOP CAN SOLVE THIS GUESS GAME EASILY. BEACUSE I DON'T KNOW WHEN THE USER WILL GUESS THE EXACT NUMBER, I WILL USE INDEFINITE WHILE LOOP. THE LOOP WILL KEEP RUNNING  INDEFINITELY UNTIL THE USER GETS  THE EXACT NUMBER USING THE RANDOM.RANDINT 


#I'M GOING TO USE INFINITE LOOP HERE BEACUSE I  WANT THE LOOP TO RUN UNTIL THE USER GUESS  THE  EXACT NUMBER. I.E, I DON'T KNOW HOW MANY TIMES THE USER WILL NOT GUESS IT RIGHT.




import random
lower = int(input("Enter a lower bound number: "))
upper = int(input("Enter a upper bound number: "))
number = random.randint(lower, upper) # THE RANDINT RETURN A  RANDOM NUMBER  IN THE GIVEN RANGE


name = input("What's your name: ")
print("Hi", name,", WELCOME to Temi's random guessing game. Feel relax and grab a cup of parfait")
user_guess  = int(input("Enter an integer btw lower t0 upper:  "))

while True: # IT WILL RUN INDEFINITELY UNTILL A BREAK STATEMENT IS FOUND
   
    if user_guess > number:
        print(number) # I WANT TO SEE THE RANDOM NUMBER(GUESS NUMBER) 
        print("Guess is too high, guess again,", name )
        user_guess  = int(input("Enter an integer btw lower to upper:  "))
    elif user_guess < number:
        # print(number)
        print("Guess is too low, guess again,", name )
        user_guess  = int(input("Enter an integer btw lower to upper:  "))
    else:
        # print(number)
        print(name,", you  guessed it right, CONGRATULATIONS.")
        break # IF THE RANDOM NUMBER IS == TO THE GUESS NUMBER, IT SHOULD STOP THE LOOP
    
