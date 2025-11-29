# write a program that find a word in a string and returns yes or no if the characters of the first word are found in the string✅
# the program should be case insensitive '✅
# Your task is to write a program which answers the following question: are the characters comprising the first string hidden inside the second string?✅

word = input("Enter a word you wish to find: ").upper()
strn = input("Enter a string you wish to search through: ").upper()

found = True
start = 0
# the key to solving this problem is treating each character of the word as a substring and checking if it is found in the string
# updating the start position ensures that the characters are checked in a sequential manner
for char in word:
    pos = strn.find(char, start)
    if pos == -1:
        found = False
        break
    start = pos + 1

if found:
    print("Yes")
else:
    print("No")


# always remember to clean the input to remove spaces and punctuations and make it case insensitive.