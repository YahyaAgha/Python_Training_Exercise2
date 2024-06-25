#exercise 2, Write a program that prints the numbers from 1 to 50. 
# For multiples of three, print "Fizz" instead of the number, and for multiples of five, print "Buzz". 
#For numbers that are multiples of both three and five, print "FizzBuzz".
non_numbers=[]
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
        non_numbers.append(number)

# Print the list of non-fizz numbers which come with else 
print("Non-FizzBuzz numbers:", non_numbers)