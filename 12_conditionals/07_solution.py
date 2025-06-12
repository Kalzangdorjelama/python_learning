# 7. Coffee Customization

# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = input("Enter a size of coffee to order: ")
extra_shot = int(input("do you want a extra_shot if yes then write 1 if not 0 : "))

if extra_shot:
    coffee = order_size + " coffee with an extra shot"
else:
    coffee = order_size + " coffee"

print(coffee)