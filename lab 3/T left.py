#Program number 8

for number in range(7):
    if number in [3, 6]:
        continue
    print(number, end=' ')

#Program number 9

def fibonacci_fizzbuzz(n):
    a, b = 0, 1
    while a <= n:
        if a % 15 == 0:
            print("FizzBuzz")
        elif a % 3 == 0:
            print("Fizz")
        elif a % 5 == 0:
            print("Buzz")
        else:
            print(a)
        a, b = b, a + b

# Generate Fibonacci series up to 50
fibonacci_fizzbuzz(50)


#Program Nmuber 10

def generate_2d_array(m, n):
    return [[i * j for j in range(n)] for i in range(m)]


rows = 3
columns = 3
array = generate_2d_array(rows, columns)
for row in array:
    print(row)


#Program number 11

# Accepts multiple lines of input and prints them in lowercase
lines = []
print("Enter text (blank line to terminate):")
while True:
    line = input()
    if line:
        lines.append(line.lower())
    else:
        break
for line in lines:
    print(line)

#Program number 12

# Accepts a sequence of binary numbers and prints those divisible by 5
binary_numbers = input("Enter binary numbers separated by a comma: ").split(',')
divisible_by_five = [num for num in binary_numbers if int(num, 2) % 5 == 0]
print(",".join(divisible_by_five))

#Program number 13

# Accepts a string and calculates the number of letters and digits
s = input("Enter a string: ")
letters = digits = 0
for char in s:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
print(f"Letters {letters}\nDigits {digits}")


#Program number 14

import re

def validate_password(password):
    if (len(password) >= 6 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[$#@]", password)):
        return True
    else:
        return False

# Example usage:
password_to_test = input("Enter the password to validate: ")
if validate_password(password_to_test):
    print("Password is valid.")
else:
    print("Password is invalid.")