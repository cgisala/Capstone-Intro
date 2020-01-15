import random

#Variable
randomNum = random.randrange(1,10)
choice = 'y'

#Input
guess = int(input("Guess a number between 1 and 10:  "))

#Loops
while(choice == 'y'):
    if guess == randomNum:
        print('Congratulation you guessed the number')
        randomNum = random.randrange(1,10) #reinitialize random number
    elif guess < randomNum:
        print('Your guess is too low')
    else:
        print('Your guess is too high')
    
    choice = input("Do you want to continue? y or n  ")  #reinitialize choice
    if choice == 'y':
         guess = int(input("Guess a number between 1 and 10:  ")) #reinitialize guess

        