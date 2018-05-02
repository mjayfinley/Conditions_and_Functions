numberInput = int(input("Please enter a number: "))

if numberInput %3 == 0 and numberInput %5 == 0:
    print("Fizz Buzz")
elif numberInput %3 == 0:
    print("Fizz")
elif numberInput %5 == 0:
    print("Buzz")
