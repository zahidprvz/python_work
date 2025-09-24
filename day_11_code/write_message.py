from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)


# 10-4 Guest

name = input("Enter your name?")
path = Path('guest.txt')
path.write_text(name)


# 10-5 Guest Book

flag = True
path = Path('guest_book.txt')
guest_book = ''

while(flag):
    name = input("If you want to be guest, write your name. Otherwise write 'no'.\n")
    if name == 'no':
        flag = False
        break
    guest_book += f"{name}\n"

path.write_text(guest_book)