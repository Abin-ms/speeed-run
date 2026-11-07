num = int(input("Enter the number : "))
if(num == 0):
    print("{num} is zero.")
elif num > 0:
    print("{num} is poisitive.")
    if num % 2 == 0:
        print("{num} is even.")
    else:
        print("{num} is odd.")
elif num < 0:
    print("{num} is Negative.")
    if num % 2 == 0:
        print("{num} is Even.")
    else:
        print("{num} is Odd.")  