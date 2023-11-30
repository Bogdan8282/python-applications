def decrypt_caesar_cipher(text, shift):
    decrypted_text = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()

            char = chr((ord(char) - shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a'))

        decrypted_text += char

    return decrypted_text

cipher_text = input("Enter the encrypted text in English: ")

while True:
    try:
        shift = int(input("Enter the shift (an integer): "))
        decrypted_result = decrypt_caesar_cipher(cipher_text, shift)
        print(f"Decrypted text: {decrypted_result}")
        break
    except ValueError:
        print("Please enter a valid value.")
