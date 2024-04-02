def is_automorphic(num):
    square = num * num
    num_str = str(num)
    square_str = str(square)
    return square_str.endswith(num_str)
print(is_automorphic(5))  # True, as 5^2 = 25
print(is_automorphic(25))  # True, as 25^2 = 625
print(is_automorphic(76))  # True, as 76^2 = 5776
print(is_automorphic(7))   # False, as 7^2 = 49
