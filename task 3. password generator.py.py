import random
import string

def generate_password(length=12):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a secure password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password you want to generate: "))
    generated_password = generate_password(password_length)
    print(f"Generated Password: {generated_password}")
