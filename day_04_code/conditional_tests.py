user = 'zahid'

print("Is user == 'zahid' ? I predict True")
print(user == 'zahid')

print("Is user == 'ali' ? I predict False")
print(user == 'ali')

# equality and inequality with strings
health = 'good'
if health == 'good':
    print("You are good to go!")
else:
    print("You have to take care of yourself!")


# using lower()
name = 'Zahid'
if name.lower() == 'zahid':
    print(f"Hello, {name}")
else:
    print("I didn't recognized you!")

# numerical tests for equality and inequality, greater than less than
# using and / or keyword

english = 98
maths = 65
chemistry = 34

if english >= 50 and maths >= 50 and chemistry >= 50:
    print("You are pass in all subjects")
else:
    print("You are fail in one or more subjects")



# an item in a list or not ?
friends = ['zulfiqar', 'umair', 'wahab', 'shazib']
if 'jahanzaib' in friends:
    print("Jahanzaib is also a friend")
else:
    print("Jahanzaib is not a friend")

# an item is not in a list
friends = ['zulfiqar', 'umair', 'wahab', 'shazib']
if 'zulfiqar' not in friends:
    print("Zulfiqar is not my friend")
else:
    print("Zulfiqar is my friend")