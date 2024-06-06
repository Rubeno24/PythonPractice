#used to open a file named sample.txt and put into read mode and names it fie
with open('sample.txt','r') as file:
    #store the content of the file inside the string named content
    content=file.read()

#dictionary to hold the key which is the word name and the value which is the number of occurences
words_count={}

#splits the the strings into a list called words
words = content.split()

#for loop to itterate through the words list
for word in words:
    #stripping the word of extra unneeded chars and making them all lowercase
    word=word.strip('.,!?")(').lower()
    #checks if the current word is in the dictionay, if it is then we increment the count by 1
    if word in words_count:
        words_count[word]+=1
    # if not we dont increment anything since its not there but we do add the word as the key
    # and make the value the number 1 since there is one word in there
    else: 
        words_count[word]=1

#used to sort the dictionary in descending order - calls the order mehtod - then words_count.items() turns the dictionary into a list of tuples,
#then we define a lambda function that sorts based on the element of the tuple, changing it x[0] makes it sort on the words in abc order,
#then we set reverse to true to sort in reverse order, getting rid of revese order sorts the tuple normally 
sorted_words_count = dict(sorted(words_count.items(), key=lambda x: x[1], reverse=True))

#for loop to print the dictionary, word and count correspond to the key value pairs in the dictionary
for word, count in sorted_words_count.items():
    #print statement to print the key valued pair of
    print(f'{word}: {count}')