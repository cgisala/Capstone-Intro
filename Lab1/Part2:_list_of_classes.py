#Variable
choice = 'y'
classes = []

#While loop
while(choice == 'y'):
    semesterClass = input("Enter a class you are taking this semester: ")
    classes.append(semesterClass)

    choice = input("Do you want to add more y or n:  ")

print('My classes for this semester:')

#Prints the answer in each line
for myClass in classes:
    print(myClass)