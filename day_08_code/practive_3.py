# # 7-8 Deli

# sandwich_orders = ['sandwich_1', 'sandwich_2', 'sandwich_3', 'sandwich_4']
# finished_sandwiches = []

# while sandwich_orders:
#     current_sandwitch = sandwich_orders.pop()

#     print(f"I made you a {current_sandwitch.title()}")

#     finished_sandwiches.append(current_sandwitch)

# print("\n")

# for sandwich in finished_sandwiches:
#     print(f"{sandwich}")


# print("\n")

# # 7-9 No Pastrami

# sandwich_orders = ['sandwich_1', 'sandwich_2', 'sandwich_3', 'sandwich_4', 'pastrami', 'pastrami', 'pastrami', 'pastrami']


# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')

# for sandwich in sandwich_orders:
#     print(sandwich)


# print("\n")

# 7-10 Dream Vacations

dream_vacations = {}
continue_flag = True

while continue_flag:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")

    dream_vacations[name] = place

    repeat = input("Would you like to let someone else respond? (yes/no): ")
    if repeat.lower() == "no":
        continue_flag = False

print("\n--- Poll Results ---")
for name, place in dream_vacations.items():
    print(f"{name} would like to visit {place}.")
