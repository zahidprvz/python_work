# 4-10 Slices
millions = list(range(1, 10))
print(f"The first three items in the list are: {millions[:3]}")

print(f"The middle three items in the list are: {millions[3:6]}")

print(f"The last three items in the list are: {millions[-3:]}")

# 4-11 My Pizzas, Your Pizzas
pizzas = [
    'Legend Dynamite',
    'Pery Pery',
    'Tikka Pizza'
]

friend_pizzas = pizzas[:]

pizzas.append("Creamy Pizza")

print("My favorite pizzas are:\n")
for pizza in pizzas:
    print(pizza)

print("\n")

friend_pizzas.append("Cheese Pizza")

print("My friend's favorite pizzas are:\n")
for f_pizza in friend_pizzas:
    print(f_pizza)

# 4-12 More Loops