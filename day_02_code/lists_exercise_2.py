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

# 3-5 One guest not coming

print("\nBut we just came to know that Faiz Ahmad Faiz could not come\n")
guests[2] = "Javed Ahmad Ghamidi"

print(guests[0])
print(guests[1])
print(guests[2])

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

del guests[0]
del guests[0]

print(f"\n{guests}\n")