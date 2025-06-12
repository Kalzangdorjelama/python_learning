# 3. Multiplication Table Printer

# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.
i = 1

for i in range(i, 11):
    if i == 5:
        continue
    for j in range(1, 11):
        print(i,"*",j,"=",i * j)
    i + 1    
 
 
# for only 3 table
# number = 3

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(number, 'x', i, '=', number * i)
