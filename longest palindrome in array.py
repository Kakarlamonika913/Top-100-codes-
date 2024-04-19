def is_palindrome(s):
    return s == s[::-1]
def longest_palindrome(arr):
    longest = ""
    for word in arr:
        if is_palindrome(word) and len(word) > len(longest):
            longest = word
    return longest
arr = ["racecar", "apple", "level", "radar", "banana"]
print("Longest palindrome:", longest_palindrome(arr))
