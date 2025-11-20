from difflib import SequenceMatcher

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

similarity = SequenceMatcher(None, str1, str2).ratio()

print(f"Similarity between the two strings: {similarity * 100:.2f}%")
