import os
import json

def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)