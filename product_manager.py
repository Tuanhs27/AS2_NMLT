import json
FILE_NAME = 'cac_san_pham.json'

def load_data():
    try:
        with open(FILE_NAME,'r',encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []