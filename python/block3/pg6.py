s1 = input("Enter the first string : ")
s2 = input("Enter the second string : ")

s1 = sorted(s1)
s2 = sorted(s2)

if(s1 == s2):
    print("s1 and s2 are anagrams.")
else:
    print("s1 and s2 are not anagrams.")