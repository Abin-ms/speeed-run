num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
print("""Before swaping
num1 = {}
num2 = {}""".format(num1,num2) )
num1 = num1+num2
num2 = num1 - num2
num1 = num1 - num2
print("""After swaping
num1 = {}
num2 = {}""".format(num1,num2) )