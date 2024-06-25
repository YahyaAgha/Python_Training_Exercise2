#Exe 6, Write a Python program that prompts the user to enter a number,
# and then prints the number of prime numbers that exist up to the number that was entered.

def is_prime(n: int):
    if n <= 1:
        return False
    for x in range (2, n):
        if n % x == 0:
          return False 
    return True

def count_primes(limit: int) -> int:
    #count prime numbers to limit
    count = 0
    for num in range(2, limit + 1):
        if is_prime(num):
            count += 1
    return count

# Prompt the user to enter a number
user_input = input("Enter a number: ")

# Check if the input is a valid integer
try:
    user_number = int(user_input)
    # Calculate and print the number of primes up to and including the number entered
    print("The count of prime numbers up to the user number", user_number, "is :", count_primes(user_number))
except ValueError:
    print("Not Valid value, please enter valud number. ")