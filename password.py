# Program to generate a random password

import random
import string

def generate_password(length):
    if length < 6:
        return "Password length should be at least 6 characters."
    
    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password has at least one character from each pool
    all_characters = lower + upper + digits + special
    password = random.choice(lower) + random.choice(upper) + random.choice(digits) + random.choice(special)

    # Fill the rest of the password length with random characters
    password += ''.join(random.choices(all_characters, k=length - 4))

    # Shuffle the password to make it more random
    password = ''.join(random.sample(password, len(password)))

    return password

# Generate a random password of length 12
password_length = 12
print("Generated Password:", generate_password(password_length))

# Time complexity is O(n)
# Space complexity is O(n)         