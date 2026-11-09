li = [2,1,4,5,3,6,7]
temp = li[0]
a = 0
for i in range(len(li)):
    for j in range(len(li) - 1):
     if(li[j] < li[j+1]):
        temp = li[j]
        li[j] = li[j+1]
        li[j+1] = temp
        

print(li)
# sorting a list uisng bubble sort.
