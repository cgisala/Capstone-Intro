#Input

#Takes in the user name
name = input("What is your name?  ")

#Takes in the user birth month 
birthMonth = input("What month were you born in?  ")
nameLength = len(name)

#Outputs the name
print(f'hello {name}')

#Outputs the birth month
print('Happy birthday month!' + birthMonth)

#Outputs number of letters in the user name
print(f'There are {nameLength} letters in your name')