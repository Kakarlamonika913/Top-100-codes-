import fnmatch

def is_match(pattern, string):
    return fnmatch.fnmatch(string, pattern)

# Example usage
pattern = "he?lo*"
string = "hello world"
print(is_match(pattern, string))  # Output: True
