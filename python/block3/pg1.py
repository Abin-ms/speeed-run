s = input("Enter the string : ")
i = 0
j = len(s) - 1
while(i < j):
    if ( s[i]!=s[j]):
        print(f"{s} is not palindrome!!!")
        break
    i+=1
    j-=1
else:
 print(f"{s} is palindrome!!!")
