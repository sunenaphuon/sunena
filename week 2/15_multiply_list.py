def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply_list([1, 2, 3, 4]))  # Output: 24
