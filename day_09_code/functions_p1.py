# 8-1 Message

def display_message():
    print("I am learning about functions in this chapter")

display_message()


print("\n")


# 8-2 Favorite Book

def favorite_book(title):
    print(f"One of my favorite books is {title}")

favorite_book("The Alchemist")


print("\n")


# 8-3 T-Shirt

def make_shirt(size, text):
    print(f"The size of t-shirt is {size} and the text written on it is: {text}")

make_shirt("Small", "Never Give Up")
make_shirt(size="Medium", text="Hold On")


print("\n")


# 8-4 Large Shirts

def make_shirt(size="Large", text="I love Python"):
    print(f"The size of t-shirt is {size} and the text written on it is: {text}")

make_shirt()
make_shirt(size="Extra Small", text="I CAN!")


print("\n")


# 8-5 Cities

def describe_cities(name, country="Pakistan"):
    print(f"{name} is in {country}")

describe_cities("Lahore")
describe_cities("New York", "United States")
describe_cities(name="Berlin", country="Germany")

print("\n")
