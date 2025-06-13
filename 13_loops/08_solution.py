# 8. Prime Number Checker

# Problem: Check if a number is prime.

# not a good Approach Assignment to do
# num = int(input("Enter a number : "))

# if num > 1:
#     for i in range(2, num + 1):
#     # print(i)
#         if num % i == 0:
#             if num == i:
#                 print(num, "is a prime number")
#                 break
#             else:
#                 print(num, "is not a prime number")
#                 break



# another way to do
# number = 28

# is_prime = True

# if number > 1:
#     for i in range(2, number):
#         if (number % i) == 0:
#             is_prime = False
#             break

# print(is_prime)




# another way to do
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        # print(i)
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
