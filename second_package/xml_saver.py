import requests
import xml.etree.ElementTree as ET

def save_xml(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()

        root = ET.fromstring(response.content)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)

        print(f"XML-дані успішно збережено у {filename}")
    
    except requests.exceptions.RequestException as err:
        print(f"Помилка запиту: {err}")
