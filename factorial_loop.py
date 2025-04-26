def factorial_loop(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial 

number = 5
result = factorial_loop(number)
print(f"Factorial of {number} is {result}")
