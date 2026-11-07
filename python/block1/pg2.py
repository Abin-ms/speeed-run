print("-----MENU-----")
print("1.Celsius to Fahrenheit.")
print("2.Fahrenheit to Celsius.")
print("3.Exit.")
choice = int(input("-----select your choice-----"))

match choice:
    case 1:
        ce = int(input("Enter the temperature in celsius : "))
        print("Temperature in Fahrenheit = {}",format((ce*9/5)+32))
    case 2:
        fh = int(input("Enter the temperature in Fahrenheit : "))
        print("Temperature in Celsius = {}".format((fh - 32)/(9/5)))
    case 3:
        exit
    case _:
        print("Invalid input")

