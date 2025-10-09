from pathlib import Path
import json

contents = Path("username.json").read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")