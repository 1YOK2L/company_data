import os
import json
from pathlib import Path
base_dir = Path(__file__).resolve().parent.parent

full_path = os.path.join(base_dir,'util','province.json')

try:
    with open(full_path, 'r') as file:
        data = json.load(file)
        print(data)
except FileNotFoundError:
    print("The file path is incorrect or the file does not exist.")
except json.JSONDecodeError:
    print("The file is not a valid JSON document.")
