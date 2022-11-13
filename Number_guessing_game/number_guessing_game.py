import random
#Taking input from user which is total range of games
top_of_range = input("Type a number: ")
#check if the number is digit or not
if top_of_range.isdigit():
    #if the number is digit then convert it into integer
    top_of_range = int(top_of_range)
    #if the number is less than zero than print the message
    if top_of_range <=0:
        print("Please type a number greater than 0 next time.")
        quit()
else:
    #if the number is not digit than print tha message
    print("Please type a number next time.")
    quit()

#random number is generated from 0 to given number
random_number = random.randint(0,top_of_range)
#we track how many attempts user take to guess the number
guesses = 0
not_won = 0
#while loop is used to run the program until user guess the number
while True:
    guesses +=1
    user_guess = input("\nMake a guess or Q to quit:")
    #if someone wants to quit the game
    if user_guess == "q" or user_guess == "Q":
        not_won += 1
        break
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

if not_won == 1:
    print("You didn't won any points because you quit the game.")
else:
    print("\nYou got it in " + str(guesses) + " guesses.")
        