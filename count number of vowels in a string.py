def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Example usage:
input_string = "Hello, World!"
print("Number of vowels:", count_vowels(input_string))
