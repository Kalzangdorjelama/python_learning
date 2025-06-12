# 2. Movie Ticket Pricing

# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = 19
# age = 10

day = "wednesday"
# day = "monday"

price = 12 if age >= 18 else 8

if day == "wednesday":
    # price = price - 2
    price -= 2

print("Ticker price for you is $",price)