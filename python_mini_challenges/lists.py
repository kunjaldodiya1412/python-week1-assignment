numbers = [4, 7, 2, 7, 9, 2]

# 1. Largest & Smallest
print("Largest:", max(numbers))
print("Smallest:", min(numbers))

# 2. Remove Duplicates
unique = list(set(numbers))
print("Unique:", unique)

# 3. Even & Odd Count
even = sum(1 for n in numbers if n % 2 == 0)
odd = len(numbers) - even
print(f"Even: {even}, Odd: {odd}")