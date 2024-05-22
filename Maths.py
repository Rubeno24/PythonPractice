import math
import random

list = [1,2,3,4,5,6,7,8,9]
num = 1.234

#the same thing as math.max in java no import required
print(max(list))

#square root of a number
print(math.sqrt(4))

#a number raised to the power of another number
print(math.pow(2,3))

#rounds the number to the decimal point you tell it to
print("The number rounded is:",round(num,2))

#returns the sum of the whole list
print("The sum of the list is",sum(list))

#returns the smallest number in the list
print("The min of the list is",min(list))

#returns the biggest number of the list
print("The max of the list is",max(list))

#returns a random number between x any y and it includes y
print("Random number between 1 and 10",random.randint(1,10))

