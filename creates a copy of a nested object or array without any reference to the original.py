import copy
original = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 99
print("Original:", original)
print("Deep Copy:", deep_copy)
