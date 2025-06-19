name = "ada lovelace"
print(name.title())
print(name.lower())
print(name.upper())

# always store the data using .lower(), and display the data which is suitable for that specific case

first_name = "Ada"
last_name = "Lovelace"

full_name = f"{first_name} {last_name}"

print(f"Hello, {full_name.title()}!")

# another important method is strip() / rstrip() / and lstrip()

# if we have whitespaces or unintentional spaces which might cause formatting issues, we can
# use string() method to remove the whitespaces from left or right side of string
# e.g, we have a string, name = " zahid ", this string contains whitespaces at the right and left sides

name = " zahid "
print(name)
print(name.strip())
print(name.rstrip())
print(name.lstrip())

# like the above example, we can also remove prefix from any string using removeprefix() method.
# if we have a website named, zarshah_url = "https://www.zarshah.store", we can use zarshah_url.removeprefix()

zarshah_url = "https://www.zarshah.store"
print(zarshah_url.removeprefix("https://")) # this will remove the https:// part from the string and show the output

# Syntax errors with strings

# apostrophe - if you use apostrophe inside a string with single quotes then you get error
# if you use apostrophe inside a string with double quotes then you don't get an error
# because inside single quotes, python interpreter interprets string from intitial single quote
# to the apostrophe as a complete string, then the remaining half part produces error

message = "One of Python's strenghts is its diverse community."
print(message)

# below way will give errors

# message = 'One of Python's strenghts is its diverse community.'
# print(message)