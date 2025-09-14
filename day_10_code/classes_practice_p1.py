# 9-1 Restaurant & Users Example

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe(self):
        print(f"Restaurant: {self.name}")
        print(f"Cuisine: {self.cuisine}")

    def open(self):
        print(f"{self.name} is now open!")


# Instantiate one restaurant
my_restaurant = Restaurant("Baba Farid Hotel", "Desi")

print(my_restaurant.name)
print(my_restaurant.cuisine)
print()

# Call methods
my_restaurant.open()
my_restaurant.describe()
print()


# 9-2 Multiple Restaurants
restaurants = [
    Restaurant("Res1", "Cuisine1"),
    Restaurant("Res2", "Cuisine2"),
    Restaurant("Res3", "Cuisine3"),
]

for r in restaurants:
    r.describe()
print()


# 9-3 User Class
class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.password = password

    def describe(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")

    def greet(self):
        print(f"Hello {self.first_name}, your email {self.email} is registered!")


# Create users
users = [
    User("zahid", "parviz", "pervaizzahid55@gmail.com", "abc123"),
    User("namal", "hussain", "inamlfatime@gmail.com", "abc123"),
    User("zulfiqar", "khan", "zulfi@gmail.com", "cba321"),
    User("umair", "rajput", "umair@gmail.com", "zyr-abc"),
]

for u in users:
    u.describe()
    u.greet()
    print()
