import random

number=input("enter a number: ")
if number.isdigit():
    number=int(number)
    if number<=0:
        print("enter a number that is greater than 0")
        quit()
else:
    print("enter a valid number")
    quit()

random_number=random.randint(0,number)

guesses=0

while guesses<3:
    guesses+=1
    user_guess=input("enter your guess: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
        
    else:
        print("enter a valid number next time")
        continue

    if user_guess==random_number:
        print("Yayy!! You've got it correct in",guesses," guesses")
        break

    elif(user_guess>random_number):
        print("Your guess is above the number")
    else:
        print("Your guess is below the number")

        
    if(guesses==3):
        print("your guesses limit is exceeded. Better luck next time :) ")
