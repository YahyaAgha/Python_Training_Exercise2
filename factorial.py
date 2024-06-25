def factorial_num(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial_num(n - 1) #recursive..

def list_factorial(numbers: list) -> list:
    return [factorial_num(num) for num in numbers]