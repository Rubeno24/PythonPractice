from typing import Counter


mylist=[1,2,3,5,6,33,534,1,1,1,1,1]
#stores a keyvalues pair of the number and its count insdie the variable a
a=Counter(mylist)
#printing a prints the keyValued pair
# example Counter({1: 6, 2: 1, 3: 1, 5: 1, 6: 1, 33: 1, 534: 1})
print(a)

#prints just the numbers
print(a.keys())

#prints the unique occurences of each number
print(a.values())