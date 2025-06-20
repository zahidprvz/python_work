# 3-8 Seeing the World

places = [
    'germany',
    'switzerland',
    'turkey',
    'netherlands',
    'afghanistan',
]

print("\n")
print(places)

print("\nSorted:\n")
print(sorted(places))

print("\nList is still in its orginal order\n")
print(places)

print("\nList in reverse order\n")
places.reverse()
print(places)

print("\nList reversed again\n")
places.reverse()
print(places)

places.sort()
print("\nSorted list, original changed\n")
print(places)

places.sort(reverse=True)
print("\nSorted list in reverse alphabetical order, original changed\n")
print(places)

# 3-9 Dinner Guests

# Had to use the reference of previously written programs
# 3-4 Guest List
guests = [
    'Jaun Elia',
    'Albert Einstein',
    'Faiz Ahmad Faiz'
]

print("\n")

print(guests[0])
print(guests[1])
print(guests[2])

print(f"\n{len(guests)} are invited to dinner as of now in 3-4\n")

# 3-5 One guest not coming

print("\nBut we just came to know that Faiz Ahmad Faiz could not come\n")
guests[2] = "Javed Ahmad Ghamidi"

print(guests[0])
print(guests[1])
print(guests[2])

print(f"\n{len(guests)} are invited to dinner as of now in 3-5\n")

# 3-6 Adding more guests

print("\nWe got a bigger table, so adding more people to invitation\n")

guests.insert(0, "Allama Iqbal")
guests.insert(2, "Manto")
guests.append("Habib Jalib")

print(guests[0])
print(guests[1])
print(guests[2])
print(guests[3])
print(guests[4])
print(guests[5])

print(f"\n{len(guests)} are invited to dinner as of now in 3-6\n")

# 3-7 Shrinking Guest List

print("\nWe are some guest from invitation\n")

removed_1 = guests.pop()
print(f"Sorry for the inconvenience, we can't invite you now: {removed_1}")

removed_2 = guests.pop()
print(f"Sorry for the inconvenience, we can't invite you now: {removed_2}")

removed_3 = guests.pop()
print(f"Sorry for the inconvenience, we can't invite you now: {removed_3}")

removed_4 = guests.pop()
print(f"Sorry for the inconvenience, we can't invite you now: {removed_4}")

print(f"\n{guests[0]}, you are coming to dinner! Make sure your presence")
print(f"{guests[1]}, you are coming to dinner! Make sure your presence\n")

print(f"\n{len(guests)} are invited to dinner as of now in 3-7\n")

del guests[0]
del guests[0]

print(f"\n{guests}\n")

print(f"\n{len(guests)} are invited to dinner as of now in 3-7\n")
