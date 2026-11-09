# Find the largest, smallest, and second largest in a list without max()/min().
listt = [1,2,3,4,5,6]
largest = listt[0]
smallest = listt[0]
for i in range(len(listt)):
    if listt[i] > largest:
        largest = listt[i]
    if listt[i] < smallest:
        smallest = listt[i]

sortted = sorted(listt)

print(largest)
print(smallest)
print(sortted[-2])
