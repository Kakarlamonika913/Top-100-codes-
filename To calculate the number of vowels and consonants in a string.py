def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in s:
        if char.isalpha(): 
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    print("Vowels:", v_count)
    print("Consonants:", c_count)
count_vowels_consonants("Hello World")
