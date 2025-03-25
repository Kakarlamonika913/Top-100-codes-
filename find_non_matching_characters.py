def find_non_matching_characters(str1, str2):

    non_matching = []

    for i in range(len(str1)):

        if str1[i] != str2[i]:

            non_matching.append(str1[i])

    return non_matching
str1="hello"
str2="Hello"
print(find_non_matching_characters(str1,str2))
