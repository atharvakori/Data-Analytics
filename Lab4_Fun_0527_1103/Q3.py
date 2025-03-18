import random

random_numbers = [random.randint(1, 100) for _ in range(5)]

max_num = max(random_numbers)
min_num = min(random_numbers)

print("Random numbers:", random_numbers)
print("Maximum number:", max_num)
print("Minimum number:", min_num)
