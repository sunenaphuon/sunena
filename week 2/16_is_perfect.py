def is_perfect(n):
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

print(is_perfect(28))  # Output: True
