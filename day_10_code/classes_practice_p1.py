# 9-1 Restaurant

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name is: {self.restaurant_name}")
        print(f"Cuisine Type is: {self.cuisine_type}")

    def open_restaurant(self):
        print("Restaurant is Open!")

# Instantiation

my_restaurant = Restaurant("Baba Farid Hotel", "Desi")

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

print("\n")

# Calling methods

my_restaurant.open_restaurant()
my_restaurant.describe_restaurant()

print("\n")


# 9-2 Three Restaurants

restaurant_1 = Restaurant("res1", "cuis1")
restaurant_2 = Restaurant("res2", "cuis2")
restaurant_3 = Restaurant("res3", "cuis3")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

print("\n")

# 9-3 Users

class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def describe_user(self):
        print(f"Name is: {self.first_name + " " + self.last_name}")
        print(f"Email is: {self.email}")
        print(f"Password is: {self.password}")

    def greet_user(self):
        print(f"Hello, {self.first_name}, Your {self.email} is registered!")


user_1 = User("zahid", "parviz", "pervaizzahid55@gmail.com", "abc123")
user_2 = User("namal", "hussain", "inamlfatime@gmail.com", "abc123")
user_3 = User("zulfiqar", "khan", "zulfi@gmail.com", "cba321")
user_4 = User("umair", "rajput", "umair@gmail.com", "zyr_abc")

user_1.describe_user()
user_1.greet_user()

print("\n")

user_2.describe_user()
user_2.greet_user()

print("\n")

user_3.describe_user()
user_3.greet_user()

print("\n")


user_4.describe_user()
user_4.greet_user()
