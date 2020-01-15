import random

#Variable
randomNum = random.randrange(1,10)  #Declares and initializes the variable
choice = 'y' #Declares and initializes the choice to 'y'

#Prompts the user to input an initial guess
guess = int(input("Guess a number between 1 and 10:  "))

#Loops
while(choice == 'y'):
    if guess == randomNum:
        print('Congratulation you guessed the number')
        randomNum = random.randrange(1,10) #reinitialize random number
    elif guess < randomNum:
        print('Your guess is too low')  #prints if the guess is less than the random number
    else:
        print('Your guess is too high') #prints if the guess is greater than the random number
    
    choice = input("Do you want to continue? y or n  ")  #Prompts the user if he or she would like to continue
    if choice == 'y':
         guess = int(input("Guess a number between 1 and 10:  ")) #Prompts the user the enter another guess

        