# 10-6 Addition + # 10-7 Addition Calculator

print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    
    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You can't add strings to a number!")
    else:
        print(answer)



# 10-8 Cats and Dogs and # 10-9 Silent Cats and Dogs

from pathlib import Path

def read_file(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # pass (we can also just pass the exception, without any output using 'pass')
        print(f"Sorry, the file {path} does not exist.")
    else:
        print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    print()
    read_file(path)


# 10-10 Common Words

def count_letter(path, word):
    line = path.read_text()
    print(f"The word '{word}' apprears {line.lower().count(word)} times approximately in the {path}")   

filenames1 = ['siddhartha.txt', 'little_women.txt']
for filename in filenames1:
    path = Path(filename)
    print()
    count_letter(path, word='the ')