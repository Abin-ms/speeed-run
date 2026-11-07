ss = input("Enter the string :")
ss = ss.lower()
vowel = 0
consonants = 0
i = 0
ln = len(ss)
while(i < ln):
    if(ss[i] in "aeiou"):
        vowel+=1
    else:
        consonants+=1
    i+=1
print(f"""Number of vowels = {vowel}
Number of consonants = {consonants}""")
