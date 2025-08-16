# 6-7 People

person_0 = {
    'name': 'zulfiqar',
    'age': 21,
    'city': 'sambrial'
}

person_1 = {
    'name': 'namal',
    'age': '23',
    'city': 'gujranwala',
}

person_2 = {
    'name': 'zahid',
    'age': '22',
    'city': 'wazirabad',
}

person_3 = {
    'name': 'umair',
    'age': '25',
    'city': 'wazirabad',
}

person_4 = {
    'name': 'wahab',
    'age': '23',
    'city': 'jalapur',
}

peoples = [person_0, person_1, person_2, person_3, person_4]

for people in peoples:
    print(people)

print("\n")

# 6-8 Pets

pet_0 = {
    'kind': 'cat',
    'owner': 'namal',
}

pet_1 = {
    'kind': 'dog',
    'owner': 'zulfiqar',
}

pet_2 = {
    'kind': 'parrot',
    'owner': 'umair',
}

pet_3 = {
    'kind': 'peigon',
    'owner': 'wahab',
}

pets = [pet_0, pet_1, pet_2, pet_3]

for pet in pets:
    print(pet)


print("\n")



# 6-9 Favorite Places

person_0 = {
    'name': 'zulfiqar',
    'age': 21,
    'city': 'sambrial'
}

person_1 = {
    'name': 'namal',
    'age': '23',
    'city': 'gujranwala',
}

person_2 = {
    'name': 'zahid',
    'age': '22',
    'city': 'wazirabad',
}

person_3 = {
    'name': 'umair',
    'age': '25',
    'city': 'wazirabad',
}

person_4 = {
    'name': 'wahab',
    'age': '23',
    'city': 'jalapur',
}

favorite_places = {
    'gakharr': [person_2],
    'careem block': [person_0, person_4],
    'home': [person_3],
}

for place, person in favorite_places.items():
    for person in person:
        print(f"{person['name']}'s favorite place is {place}")

print("\n")



# 6-10 Favorite Numbers

favorite_numbers = {
    'zahid': [5, 7],
    'namal': [108, 22, 13],
    'ali': [0],
}

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(f"{name}'s favorite number are: \t{numbers}")
    else:
        print(f"{name}'s favorite number is \t{numbers}")



# 6-11 Cities

print("\n")


lahore = {
    'country': 'Pakistan',
    'population': 250000000,
    'fact': 'oldest city in pakistan'
}

rome = {
    'country': 'Italy',
    'population': 10000000,
    'fact': 'oldest city in italy'
}

dhaka = {
    'country': 'Bangladesh',
    'population': 80000000,
    'fact': 'oldest city in bangladesh'
}


cities = {
    'rome': rome,
    'lahore': lahore,
    'dhaka': dhaka,
}

for city, info in cities.items():
    print(f"City: {city}\nInformation: {info}\n")



# 6-12 Extensions

