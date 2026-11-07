s = input("Enter the string : ")
rev = s[::-1]
if(s == rev):
    print(f"{s} is palindrome!!!" )
else:
    print(f"{s} is not palindrome!!!")