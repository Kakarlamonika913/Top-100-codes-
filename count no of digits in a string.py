import re
def find_sum(str1):
    return sum(map(int, re.findall('\d+', str1)))
str1 = "12Prep20insta68"
print("Sum of all the digits",find_sum(str1))
