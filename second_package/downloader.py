import requests

def download_page(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        
        print(f"Сторінка успішно завантажена та збережена у {filename}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP помилка: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Помилка з'єднання: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Помилка часу очікування: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Інша помилка: {req_err}")
