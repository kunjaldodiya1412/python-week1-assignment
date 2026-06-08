# 1. String Reverse
text = input("Enter text: ")
print("Reversed:", text[::-1])

# 2. Vowel Count
vowels = "aeiouAEIOU"
count = sum(1 for c in text if c in vowels)
print("Vowel Count:", count)

# 3. Palindrome Check
if text == text[::-1]:
    print("Palindrome: Yes")
else:
    print("Palindrome: No")