# Count the frequency of each character.
ss = input("Enter the string : ")
freq = {}
i = 0
while i < len(ss):
    if ss[i] in freq:
        freq[ss[i]]+=1
    else:
        freq[ss[i]]=1
    i+=1
print(freq)
for key,values in freq.items():
    print(key,"=",values)
