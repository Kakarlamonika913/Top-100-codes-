def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count
text = "This is a sample text with vowels"
print("Number of vowels:", count_vowels(text))
