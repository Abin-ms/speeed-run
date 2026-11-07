# multiplication table generator.
num = int(input("Enter the number : "))
r = int(input("Enter the range : "))

for i in range(1,r+1):
    print("""  {}  *  {} = {}""".format(i,num,i*num))
