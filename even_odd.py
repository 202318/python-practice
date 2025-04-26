def even_odd_checker(number):
    if number % 2 ==0:
        return "Even"
    else:
        return "Odd"

num = 7
result = even_odd_checker(num)
print(f"{num} is {result}")
