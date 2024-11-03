# Варіант 2: Redis (ключ-значення)
# 1. Збереження сесій користувачів:

# Створіть просту модель сесій користувачів для веб-додатку, використовуючи Redis для зберігання стану користувачів. Наприклад, зберігайте такі дані: user_id, session_token, login_time.
# 2. CRUD операції:

# Create: Додайте нову сесію для користувача.
# Read: Отримайте активну сесію для конкретного користувача.
# Update: Оновіть час останньої активності користувача.
# Delete: Видаліть сесію після виходу користувача з системи.
# 3. TTL (Time to Live):

# Налаштуйте час життя сесії користувача. Автоматично видаляйте сесію, якщо користувач не активний більше 30 хвилин.

import redis
from datetime import datetime, timedelta
import json

"""
Підключення до Redis
"""
client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

"""
Встановлюємо час життя сесії у секундах (30 хвилин)
"""
SESSION_TTL = 1800  

"""
CREATE:
"""
def create_session(user_id, session_token):
    session_data = {
        "user_id": user_id,
        "session_token": session_token,
        "login_time": datetime.now().isoformat()
    }
    
    # Зберігаємо сесію як JSON-об'єкт і задаємо TTL 
    client.setex(session_token, SESSION_TTL, json.dumps(session_data))
    print(f"Сесія для користувача {user_id} створена.")

"""
READ:
"""
def get_session(session_token):
    session_data = client.get(session_token)
    if session_data:
        return json.loads(session_data)
    else:
        print("Сесія не знайдена або завершилася.")
        return None
"""
UPDATE:
"""
def update_session_activity(session_token):
    session_data = get_session(session_token)
    if session_data:
        session_data["last_activity_time"] = datetime.now().isoformat()
        
        # Оновлюємо сесію з новим TTL
        client.setex(session_token, SESSION_TTL, json.dumps(session_data))
        print("Час активності сесії оновлено.")
    else:
        print("Сесія не знайдена або завершилася.")

"""
DELETE:
"""
def delete_session(session_token):
    client.delete(session_token)
    print(f"Сесія з токеном {session_token} видалена.")

session_token = "test_session_token"
create_session(user_id="123", session_token=session_token)

print("Залишок TTL після створення сесії:", client.ttl(session_token))  

update_session_activity(session_token)
print("Залишок TTL після оновлення активності:", client.ttl(session_token))  

delete_session(session_token)
print("Спроба отримати сесію після видалення:", get_session(session_token))  