str1=input("enter string 1")
str2=input("enter string 2")
if len(str1)!=len(str2):
    print("not anagram")
else:
    if sorted(str1)==sorted(str2):
        print("anagram")
    else:
        print("not ")
