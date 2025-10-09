from pathlib import Path
import json

path = Path("numbers.json")
contents = path.read_text()
numbers = json.loads(contents)
print(f"Read numbers from {path.resolve()}: {numbers}")