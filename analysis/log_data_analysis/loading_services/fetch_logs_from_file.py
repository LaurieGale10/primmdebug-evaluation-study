import json

def fetch_data_from_json(file_path: str) -> list[dict]:
    with open(f"{file_path}.json", 'r') as file:
        data = json.load(file)
    return data