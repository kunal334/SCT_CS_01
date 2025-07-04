def caesar_cipher(text, shift, mode='encrypt'):
    """
    Encrypt or decrypt text using the Caesar cipher.
    
    Parameters:
        text (str): The input string to encrypt or decrypt.
        shift (int): The shift value for the cipher.
        mode (str): 'encrypt' or 'decrypt'.
    
    Returns:
        str: The resulting encrypted or decrypted text.
    """
    if mode == 'decrypt':
        shift = -shift

    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # alphabetical index 0-25
            alpha_index = ord(char) - start
            # shifted index with wrap-around
            shifted_index = (alpha_index + shift) % 26
            result.append(chr(start + shifted_index))
        else:
            # non-alphabetical characters unchanged
            result.append(char)
    return ''.join(result)


def main():
    print("=== Caesar Cipher Encryption / Decryption ===")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ").strip()

        if choice == '1' or choice == '2':
            mode = 'encrypt' if choice == '1' else 'decrypt'
            message = input("Enter your message: ")
            while True:
                shift_input = input("Enter shift value (integer): ").strip()
                if shift_input.lstrip('-').isdigit():
                    shift = int(shift_input)
                    break
                else:
                    print("Invalid shift. Please enter an integer value.")

            output = caesar_cipher(message, shift, mode)
            if mode == 'encrypt':
                print(f"\nEncrypted message:\n{output}")
            else:
                print(f"\nDecrypted message:\n{output}")

        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
