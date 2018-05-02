numberInput = int(input("Please enter a number: "))

if numberInput == 0:
    print("This number is neither odd or even.")
elif numberInput %2 == 0:
    print("This number is even")
else:
    print("This number is odd")
