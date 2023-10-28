def encrypt(text, shift, password):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_amount + shift) % 26 + shift_amount)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text, password

def decrypt(text, shift, password):
    if password != "your_password_here":
        return "Invalid password. Decryption failed."

    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Enter 'e' for encryption or 'd' for decryption: ")
    if choice == 'e':
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value (e.g., 3 for Caesar cipher): ")
        password = input("Set a password for decryption: ")
        
        encrypted_text, password = encrypt(text, shift, password)
        print(f"Encrypted Text: {encrypted_text}")
        print(f"Password for decryption: {password}")
    elif choice == 'd':
        text = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value (e.g., 3 for Caesar cipher): ")
        password = input("Enter the password for decryption: ")

        decrypted_text = decrypt(text, shift, password)
        print(f"Decrypted Text: {decrypted_text}")
    else:
        print("Invalid choice. Use 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
