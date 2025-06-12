# 6. Factorial Calculator

# Problem: Compute the factorial of a number using a while loop.

nums = int(input("Enter a number: "))  
factorial = 1

if nums == 0:
    factorial = 1
else:
    while nums > 0:
        factorial *= nums
        nums -= 1

print("The factorial is:", factorial)
