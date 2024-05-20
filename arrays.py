print("Hello World")

#define an array of numbers in pyhton
intlist = [1,2,3,4,5,6,7,8,9]

#define an array of strings in python
basketballPlayers = ["Ruben","Lebron","Kobe"]

#print the names of all basketball players in pyhton on the same line since
#we are setting the end stirng to an empty string and not a new line \n
for names in basketballPlayers:
    print(names, end=" ")

#calling the print statement so it places a new line for us
print()


#for loop to print all the elements of the list with a new line after every number
#by default the print statement has end='\n'
for nums in intlist:
    print(nums)

#for loop in python to print the elements of the a
for nums in intlist:
    print(nums , end=' ')

print()

