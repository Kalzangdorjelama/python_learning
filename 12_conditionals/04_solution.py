# 4. Fruit Ripeness Checker

# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

# fruit = "Banana"
# color = "Yellow"

fruit = input("Enter a fruit name : ")
color = input("Enter a color of fruit : ")

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
else:
     print("Given",fruit,"fruit information is not found 🥺")   