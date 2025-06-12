# 5. Weather Activity Suggestion

# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = input("Enter a weather situation : ")

if weather == "Sunny":
    print("Go for a walk")
elif weather == "Rainy":
    print("Read a book")
elif weather == "Snowy":
    print("Build a snowman")
else:
    print("Given",weather,"weather information is not found 🥺")


# another way to do
# weather = "Sunny"

# if weather == "Sunny":
#     activity = "Go for a walk"
# elif weather == "Rainy":
#     activity = "Read a book"
# elif weather == "Snowy":
#     activity = "Build a snowman"

# print(activity)
