def frequency_char(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq
s=input()
freq=frequency_char(s)
print(freq)
