def is_palindrome(s):
    return s == s[::-1]  
def longest_palindrome(arr):
    palindromes = [word for word in arr if is_palindrome(word)]  
    if palindromes: 
        return max(palindromes, key=len)  
    return None  
arr = ["racecar", "apple", "madam", "banana", "noon"] 
longest = longest_palindrome(arr)  
print("Longest palindrome:", longest)  
