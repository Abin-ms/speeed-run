num = int (input("Enter a number :"))
a = 0
b = 1
while(num!=0):
    print(a,end=" ")

    c = a + b
    a = b
    b = c
    num-=1