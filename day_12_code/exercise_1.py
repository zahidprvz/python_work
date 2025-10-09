# 10-11. Favorite Number + 10-12. Favorite Number Remembered

from pathlib import Path
import json

path = Path("favorite_number.json")

def get_favorite_number():
    """Prompt for and store the user's favorite number."""
    favorite_number = input("What is your favorite number? ")
    contents = json.dumps(favorite_number)
    path.write_text(contents)
    print(f"We'll remember your favorite number when you come back, {favorite_number}!")

def read_favorite_number():
    """Read and return the user's favorite number if it exists."""
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        print(f"Your favorite number is {favorite_number}.")
    else:
        get_favorite_number()

read_favorite_number()