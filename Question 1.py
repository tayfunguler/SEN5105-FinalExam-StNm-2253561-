# SEN5105 - Introduction to Programming - Python
# Caesar Cipher Encryption and Decryption Program
# Developed by: Tayfun Guler

def caesar_cipher(text, key, mode):
    """
    Encrypt or decrypt the text using the Caesar Cipher.
    This function shifts each letter by the number specified by 'key'.
    """
    # Adjust the key if we're decrypting
    if mode == 'decrypt':
        key = -key

    result = ""

    # Loop through each character in the text
    for char in text:
        # If it's a letter, shift its ASCII value
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            # Shift the character and wrap around the alphabet
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            # If it's not a letter, leave it as it is
            result += char

    return result

def main():
    # Ask the user whether they want to encrypt or decrypt
    mode = input("Do you want to (e)ncrypt or (d)ecrypt? > ")
    if mode.lower() in ('e', 'encrypt', 'd', 'decrypt'):
        key = int(input("Please enter the key (0 to 25) to use. > "))
        message = input("Enter the message to {}. > ".format("encrypt" if mode in ('e', 'encrypt') else "decrypt"))
        # Perform the encryption/decryption
        processed_text = caesar_cipher(message, key, "encrypt" if mode in ('e', 'encrypt') else "decrypt")
        print(f"Processed text: {processed_text}\n")
    else:
        print("Invalid mode selected. Please choose 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
