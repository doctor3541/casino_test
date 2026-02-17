import json

def save_game(data, file="save.json"):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def load_game(file="save.json"):
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return None
