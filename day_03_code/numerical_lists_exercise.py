# 4-3 Counting to Twenty
for i in range(1, 21):
    print(i)

print("\n")


# 4-4 One Million
millions = list(range(1, 1000001))

# print(millions)

print("\n")


# 4-5 Summing a Million
print(min(millions))
print("\n")
print(max(millions))
print("\n")
print(sum(millions))

# 4-6 Odd Numbers
for i in range(1, 21, 2):
    print(i)

print("\n")

# 4-7 Threes
numbers = []
for i in range(3, 31, 3):
    number = numbers.append(i)

print(numbers)

print("\n")

# 4-8 Cubes
cubes = []
for i in range(1, 11):
    cube = cubes.append(i ** 3)

print(cubes)

print("\n")

# 4-9 Cube Comprehension
cubes = [value ** 3 for value in range(1, 11)]
print(cubes)