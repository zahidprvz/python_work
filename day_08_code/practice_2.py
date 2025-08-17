# 7-4 Pizza Toppings

# topping = ""
# prompt = "Enter a pizza topping to add"
# prompt += "\n(Enter 'quit' when finished adding!): "

# while topping != "quit":
#     if topping != "":
#         print(f"{topping} will be added.\n")
#     topping = input(prompt)
    


# 7-5 Movie Tickets

age = 0
fair = 0
prompt = "You want a ticket?"
prompt += "If yes write your age, if no write -1: " 

while age != '-1':
    age = input(prompt)

    if int(age) <= 3 and int(age) > 0:
        fair = 0
        print("The ticket is free")
    elif int(age) > 3 and int(age) < 12:
        fair = 10
        print(f"The ticket is {fair}$")
    elif int(age) >= 12:
        fair = 15
        print(f"The ticket is {fair}$")


