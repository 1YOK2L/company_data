import os
import json
from pathlib import Path
from company.models import Subdistrict

base_dir = Path(__file__).resolve().parent.parent
full_path = os.path.join(base_dir, "util", "subdistrict.json")


def load_json_data():
    try:
        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)

            for subdistrict in data:
                Subdistrict.objects.get_or_create(
                    name_en=subdistrict["name_en"],
                    defaults={
                        "name_th": subdistrict["name_th"],
                    },
                )

        print(f"Imported {len(data)} subdistricts.")

    except FileNotFoundError:
        print("The file path is incorrect or the file does not exist.")
    except json.JSONDecodeError:
        print("The file is not a valid JSON document.")