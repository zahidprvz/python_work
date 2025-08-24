# 9-4 Number Served

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant Name is: {self.restaurant_name}")
        print(f"Cuisine Type is: {self.cuisine_type}")
        print(f"Numbers Served: {self.number_served}")

    def open_restaurant(self):
        print("Restaurant is Open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment

restaurant = Restaurant("Ganj Shakar Hotel", "Desi")
restaurant.describe_restaurant()

print("\n")

restaurant.number_served = 5
restaurant.describe_restaurant()

print("\n")

restaurant.set_number_served(10)
restaurant.describe_restaurant()

print("\n")
restaurant.increment_number_served(5)
restaurant.describe_restaurant()


# 9-5 Login Attempts

class User:
    def __init__(self, first_name, last_name, email, password, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.login_attempts = login_attempts

    def describe_user(self):
        print(f"Name is: {self.first_name + " " + self.last_name}")
        print(f"Email is: {self.email}")
        print(f"Password is: {self.password}")
        print(f"Login Attempts are: {self.login_attempts}")

    def greet_user(self):
        print(f"Hello, {self.first_name}, Your {self.email} is registered!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user_1 = User("namal", "hussain", "inamlfatime@gmail.com", "abc123", 2)


user_1.describe_user()
user_1.greet_user()

print("\n")

user_1.increment_login_attempts()
user_1.describe_user()

print("\n")

user_1.reset_login_attempts()
user_1.describe_user()

#

