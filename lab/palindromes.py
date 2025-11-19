#palindrome is a word that reads the same forwards and backwards.
#write a function that checks if a word is a palindrome. ✅
#the function should return True if the word is a palindrome, False otherwise.✅
#the function should be case insensitive.✅
#the function should ignore spaces and punctuation.✅

def is_palindrome():
    word = input("Enter a word: ").lower().replace(" ","")
    word2 = word[::-1]

    if word == word2:
        return "It'S a palindrome"
    else:
        return "It's not a palindrome"

print(is_palindrome())