# 10-1 Learning Python

from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

print(contents)

print()

list_contents = contents.splitlines()

for list_content in list_contents:
    print(list_content)


# 8-2 Learning C

updated_contents = contents.replace('Python', 'C')
print()
print(updated_contents)
print()

# 8-3 Simpler Code

for content in contents.splitlines():
    print(content)