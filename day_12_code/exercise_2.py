# 10-13. User Dictionary

from pathlib import Path
import json

def get_stored_userinfo(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_userinfo(path):
    """Prompt for a new username and store it."""
    username = input("What is your name? ")
    age = input("How old are you? ")
    favorite_color = input("What is your favorite color? ")
    user_info = {"name": username, "age": age, "favorite_color": favorite_color}

    contents = json.dumps(user_info)
    path.write_text(contents)
    return contents

def greet_user():
    """Greet the user by name."""
    path = Path("user_info.json")
    user_info = get_stored_userinfo(path)

    if user_info:
        print(f"Welcome back, {user_info}!")
    else:
        username = input("What is your name? ")
        age = input("How old are you? ")
        favorite_color = input("What is your favorite color? ")
        user_info = {"name": username, "age": age, "favorite_color": favorite_color}
        
        contents = json.dumps(user_info)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()