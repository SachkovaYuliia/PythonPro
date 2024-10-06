import requests
import json

def save_json(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        
        print(f"JSON-дані успішно збережено у {filename}")
    
    except requests.exceptions.RequestException as err:
        print(f"Помилка запиту: {err}")
