# Capitalize the first letter of every word without using .title()
st = input("Enter the string : ")
result = ""
cap_next = True
for s in st:
    if s == " ":
        result+=s
        cap_next = True
    elif cap_next:
        result+=s.upper()
        cap_next = False
    else:
        result+=s
print(result)