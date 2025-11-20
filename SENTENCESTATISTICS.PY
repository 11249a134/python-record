def sentence_statistics(sentence):
    words = len(sentence.split())
    digits = 0
    uppercase = 0
    lowercase = 0

    for ch in sentence:
        if ch.isdigit():
            digits += 1
        elif ch.isupper():
            uppercase += 1
        elif ch.islower():
            lowercase += 1

    return words, digits, uppercase, lowercase

sentence = input("Enter a sentence: ")

words, digits, uppercase, lowercase = sentence_statistics(sentence)

print("\n--- Sentence Statistics ---")
print(f"Number of Words: {words}")
print(f"Number of Digits: {digits}")
print(f"Number of Uppercase Letters: {uppercase}")
print(f"Number of Lowercase Letters: {lowercase}")
