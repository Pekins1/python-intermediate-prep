# improve the caesar cipher to handle upper and lower case letters ✅
# ask the user for a shift value from 1 to 25 inclusive and repeat the process if the user enters an invalid value ✅
# ask the user for a message to encrypt ✅


def cipher():
    text = input("Enter a message to encrypt: ")
    shift = 0
    
    while shift < 1 or shift > 25:
        try:
            shift = int(input("Enter a shift: "))
            if shift < 1 or shift > 25:
                print("Invalid shift value. Please enter a number between 1 and 25.")
        except ValueError:
            print("Invalid shift value. Please enter a number between 1 and 25.")

    encrypted_text = ""
    for char in text:
        if not char.isalpha():
            encrypted_text += char
            continue
        
        if char.isupper():
            encrypted_text += chr((ord(char) - 65 + shift)% 26 + 65) # 65 is the ASCII value of 'A' it loops back to the beginning of the alphabet if the shift is greater than 26
        else:
            encrypted_text += chr((ord(char) - 97 + shift)% 26 + 97) # 97 is the ASCII value of 'a' it loops back to the beginning of the alphabet if the shift is greater than 26
    
    return encrypted_text

print(cipher())
