# 1. Character Frequency
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print("Frequency:", freq)

# 2. Max Value Key
marks = {"Amit": 88, "Neha": 95, "Raj": 76}
topper = max(marks, key=marks.get)
print("Topper:", topper)

# 3. Merge Two Dicts
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged = {**dict1, **dict2}
print("Merged:", merged)