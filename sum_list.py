def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

sample_list = [1, 2, 3, 4, 5]
result = sum_list(sample_list)
print("Sum of list", result)
