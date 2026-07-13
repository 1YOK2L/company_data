import os
import json
from pathlib import Path
from company.models import Province

base_dir = Path(__file__).resolve().parent.parent

full_path = os.path.join(base_dir, 'util', 'province.json')

def load_json_data():
    try:
        with open(full_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                name_th = item.get('name_th')
                name_en = item.get('name_en')

                if name_th and name_en:
                    Province.objects.get_or_create(name_th=name_th, name_en=name_en)

    except FileNotFoundError:
        print("The file path is incorrect or the file does not exist.")
    except json.JSONDecodeError:
        print("The file is not a valid JSON document.")