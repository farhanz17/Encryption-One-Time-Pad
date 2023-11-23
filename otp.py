import random

def text_to_binary(text):
    """Convert a text (letters) to binary."""
    binary_text = ''.join(format(ord(char), '08b') for char in text)
    return binary_text

def binary_to_text(binary_text):
    """Convert binary to text."""
    text = ''.join(chr(int(binary_text[i:i+8], 2)) for i in range(0, len(binary_text), 8))
    return text

def generate_key(length):
    """Generate a random key of the specified length."""
    key = [random.choice('01') for _ in range(length)]
    return ''.join(key)

def encrypt(plaintext, key):
    """Encrypt the plaintext using the one-time pad."""
    ciphertext = ''
    for i in range(len(plaintext)):
        # XOR operation between the binary representation of plaintext and key
        encrypted_bit = bin(int(plaintext[i], 2) ^ int(key[i], 2))[2:].zfill(8)
        ciphertext += encrypted_bit
    return ciphertext

def main():
    # Input plaintext
    plaintext = input("Masukkan plaintext: ")

    # Convert plaintext to binary
    binary_plaintext = text_to_binary(plaintext)

    # Generate a key of the same length as the binary plaintext
    key = generate_key(len(binary_plaintext))

    # Encrypt the binary plaintext using the one-time pad
    ciphertext = encrypt(binary_plaintext, key)

    # Print the results
    print(f"\nPlaintext: {plaintext}")
    print(f"Plaintext (binary): {binary_plaintext}")
    print(f"Key (binary): {key}")
    print(f"Ciphertext (binary): {ciphertext}")

    # Convert the key to text for better readability
    key_text = binary_to_text(key)
    print(f"Key (text): {key_text}")

if __name__ == "__main__":
    main()
