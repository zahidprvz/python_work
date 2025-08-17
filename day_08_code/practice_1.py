# 7-1 Rental Car

rental_car_kind = input('What kind of rental car do you want? ')
print(f"Let me see if I can find you a {rental_car_kind}")



print("\n")



# 7-2 Restaurant Seating

number_people = int(input("How many people are in their dinner group? "))

if number_people > 8:
    print("They will have to wait for a table")
else:
    print("Your table is ready")


print("\n")


# 7-3 Multiples of Ten

number = int(input("Enter a number: "))

if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")

 