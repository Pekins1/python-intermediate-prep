# anagrams are words that have the same letters in the same quantity, but in a different order.
# Objective: Write a function that checks if two words are anagrams.
# The function should ask for two words from the user.✅
# The function should return anagrams or not anagrams.✅
# The function should check if the words are the same length.✅
# The function should check character counts for each word.✅
# The function should ignore spaces and punctuation.
import string

def clean_word(word):
    word = word.lower()
    return "".join(char for char in word if char in string.ascii_lowercase)

def is_anagram():
    word1 = list(input("Enter first word: ").lower())
    word2 = list(input("Enter second word: ").lower())

    # check if the words are the same length
    if len(word1) != len(word2):
        return "not anagrams"

    # check character counts for each word
    char_count1 = {}
    char_count2 = {}


    for char in word1:
        char_count1[char] = char_count1.get(char, 0) + 1 # this is a dictionary that counts the number of times each character appears in the word
        # char_count1[char], char is the key and char_count1.get(char, 0) is the value. if the character is not in the dictionary, it will add it with a value of 0.
        # char_count1.get(char, 0) is the value, value is the number of times the character appears in the word. if the character is not in the dictionary, it will add it with a value of 0.
    for char in word2:
        char_count2[char] = char_count2.get(char, 0) + 1 

    if char_count1 == char_count2: # this is a comparison of the two dictionaries
        return "anagrams"
    else:
        return "not anagrams"

print(is_anagram())