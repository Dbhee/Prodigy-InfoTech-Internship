#Python program to encrypt and decrypt using Caesar cipher Algorithm. 
def caesar_cipher(text, key, mode):
    """
    text = the input text to be encrypt or decrypt.
    key = the number of position to shift each character.
    mode = encrypt or decrypt
    """
    result = ""
    key = key if mode == "encrypt" else -key #Adjust key for decryption.
    for char in text:
        if char.isalpha(): #Only shift alphabetic characters
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char #Non-alphabetical characters remain the same

    return result

def main():
    """
    Main function to prompt user for input, perform encryption and decryption,
    and display the results.
    """
    text = input("Enter the text you want to encrypt: ")
    key = int(input("Enter the shift value: "))


    #encrypt
    encrypted_text = caesar_cipher(text, key, "encrypt")
    print(f"Encrypted: {encrypted_text}")
    #decrypt
    decrypted_text = caesar_cipher(encrypted_text, key, "decrypt")
    print(f"Decrypted: {decrypted_text}")
    


main()