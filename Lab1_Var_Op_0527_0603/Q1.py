def multiply_and_add(a, b):
    result_multiplication = a * b
    result_sum = a + b
    
    return result_multiplication, result_sum

num1 = 5
num2 = 3

mul, summ = multiply_and_add(num1, num2)

print("Multiplication is:", mul)
print("Sum is:", summ)