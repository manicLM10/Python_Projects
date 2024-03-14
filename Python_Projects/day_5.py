import random
import string

def generate_password(letters,symbols,numbers):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    res1 = ''.join(random.choice(string.digits) for i in range(numbers))
    res2 = ''.join(random.choice(string.punctuation) for i in range(symbols))
    temp = letters - symbols + numbers
    res3 = ''.join(random.choice(string.ascii_letters) for i in range(temp))
    password = ''.join(res1+res2+res3)
    
    shuffled_password = list(password)
    random.shuffle(shuffled_password)
    return ''.join(shuffled_password)


letters = int(input("Enter the lenght of your password \n"))
symbols = int(input("Enter the how many symbols would u like : \n"))
numbers = int(input("Enter the how many numbers would u like : \n"))

print(generate_password(letters,symbols,numbers))