# 10. Pet Food Recommendation

# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_species = input("Enter a pet species name : ")

pet_age = int(input("Enter a pet species age : "))

if pet_species == "Dog":
    if pet_age < 2:
        print("Junior Puppy food")
    elif pet_age >= 2:
        print("Senior Puppy food")
elif pet_species == "Cat":
    if pet_age < 5:
        print("Junior cat food")
    elif pet_age >= 5:
        print("Senior cat food")
else:
    print("This",pet_species,"species information not found 🥺")