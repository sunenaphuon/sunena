import random

def generate_random_numbers():
    return [random.randint(0, 100) for _ in range(4)]

print(generate_random_numbers())  # Example output: [42, 17, 8, 99]
