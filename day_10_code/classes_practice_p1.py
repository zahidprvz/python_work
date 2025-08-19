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
