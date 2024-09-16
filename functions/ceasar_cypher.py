alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Get user inputs
encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar_encryption(original_text, shift_amount, encode_decode):
    """
    Encrypts or decrypts a given text by shifting its letters according to a shift amount, 
    a.k.a 'Caesar Cypher'.
    
    This function shifts each letter of the input text based on its position in the alphabet. 
    The direction of the shift depends on whether the user wants to 'encode' (shift forward) or 
    'decode' (shift backward) the text.

    Args:
        original_text (str): The text to be encrypted or decrypted.
        shift_amount (int): The number of positions to shift the letters by in the alphabet.
        direction (str): Either 'encode' to shift forward or 'decode' to shift backward.

    Returns:
        str: The resulting encrypted or decrypted text after applying the shift.
    """
    encrypted_text = ""
    shift_amount %= 26  # Ensure the shift doesn't exceed the length of the alphabet

    if encode_decode == "decode":
        shift_amount = -shift_amount

    for letter in original_text:
        if letter in alphabet:
            # Find the position of the letter in the alphabet
            position = alphabet.index(letter)
            # Calculate the new position with the shift
            new_position = (position + shift_amount) % 26
            # Append the shifted letter to the result
            encrypted_text += alphabet[new_position]
        else:
            # If the character is not in the alphabet, just add it unchanged
            encrypted_text += letter

    return encrypted_text


# Call the function and print the result
result = caesar_encryption(text, shift, encode_decode)
print(f"The {encode_decode}d text is: {result}")
