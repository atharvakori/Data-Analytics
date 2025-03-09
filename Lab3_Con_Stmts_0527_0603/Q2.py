a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = a if a > b and a > c else (b if b > c else c)

print("The largest number is:", largest)