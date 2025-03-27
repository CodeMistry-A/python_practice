 
'''
for num in range(1, 10):  # Loop from 1 to 50
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")  # Divisible by both 3 and 5
    elif num % 3 == 0:
        print("Fizz")  # Divisible by 3
    elif num % 5 == 0:
        print("Buzz")  # Divisible by 5
    else:
        print(num)  # Print the number if none of the above


name = input("Enter your name: ")
print("Hello, " + name)


# Simple Calculator
'''
# Get user input
num1 = int(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = int(input("Enter second number: "))

# Perform calculation
if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operator!")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum_result = num1 + num2

print("The sum is:", sum_result)



import random

secret_number = random.randint(1, 10)  # Random number between 1 and 10
attempts = 0

print("Welcome to 'Guess the Number'!")
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
