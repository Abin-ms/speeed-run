import random

r = random.randint(1,100)

re = True
while(re == True):
    user_choice = int(input("Enter your choice : "))
    if(user_choice == r):
        re = False
        print("Congratulations you won!!!!")
        break
    elif (user_choice > r):
        print("Your choice is higher than the number...")
    elif(user_choice < r):
        print("Your choice is Lesser than the number...")
