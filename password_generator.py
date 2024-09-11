import random
import string


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


# Example usage
password = generate_password(16)  # 16 belgili parol
print("Generated Password:", password)
