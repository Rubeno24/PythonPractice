print("Hello World")

#define an array of numbers in pyhton
intlist = [1,2,3,4,5,6,7,8,9]

#define an array of strings in python
basketballPlayers = ["Curry","Lebron","Kobe"]

#print the names of all basketball players in pyhton on the same line since
#we are setting the end stirng to an empty string and not a new line \n
for names in basketballPlayers:
    print(names, end=" ")

#calling the print statement so it places a new line for us
print()

#adding a number to an array in the beggining
intlist.insert(0,100)

#Appending to the end of an array
intlist.append(200)

#remove from the array by passing in a value
intlist.remove(5)

#removes from the array by passing in an index
del intlist[0]

basketballPlayers[0]= "Shaq"

#sort an array
intlist.sort()

#returns a copy of the array that was sorted
sortedlist = sorted(intlist)

#returns how long the list is
print("The lenght of the list is:",len(intlist))

#reverses the list, first call the method then the list will be reversed then you can print the list
intlist.reverse()
print("This is the list reversed",intlist)

#for loop to print all the elements of the list with a new line after every number
#by default the print statement has end='\n'
for nums in intlist:
    print(nums)

#for loop in python to print the elements of the a
for nums in intlist:
    print(nums , end=' ')

print()



#the exact same to array[i] in java
print("Prints the first element of the basketball players list:",basketballPlayers[0])

#slices the array and returns the new array based on the bounds you give it
print("The first 6 numbers of the intlist array",intlist[0:5])