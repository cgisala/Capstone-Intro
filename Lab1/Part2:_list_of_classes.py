#Variable
choice = 'y'  #Initializes choice to y
classes = []  #Declares an empty array

#Loops until the user enters 'n' for no
while(choice == 'y'):
    semesterClass = input("Enter a class you are taking this semester: ")
    classes.append(semesterClass)

    choice = input("Do you want to add more y or n:  ")

print('My classes for this semester:') 

#Prints the answer in each line
for myClass in classes:
    print(myClass)