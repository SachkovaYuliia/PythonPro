# Частина 2: Порівняння SQL і NoSQL
# Виконайте порівняння між реляційною базою даних (наприклад, PostgreSQL) та NoSQL (наприклад, MongoDB):
# Виконайте аналогічні CRUD операції для однієї й тієї ж моделі даних.
# Проаналізуйте переваги та недоліки кожної системи для різних завдань.

# import psycopg2
# from psycopg2 import sql
# from datetime import datetime 
# from dotenv import load_dotenv
# import os

# load_dotenv()

# conn = psycopg2.connect(
#     host=os.getenv("LOCALHOST"),
#     database=os.getenv("DB_NAME"),
#     user=os.getenv("USER_NAME"),
#     password=os.getenv("DB_RASST")
# )

# cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         user_id SERIAL PRIMARY KEY,
#         name VARCHAR(100),
#         email VARCHAR(100) UNIQUE,
#         created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#     )
# """)
# conn.commit()

# print("Таблиця users створена.")

# cursor.execute("""
#     INSERT INTO users (name, email) VALUES (%s, %s)
# """, ('Test', 'test@gmail.com'))
# conn.commit()
# print("Користувач доданий.")

# cursor.execute("""
#     SELECT * FROM users WHERE email = %s
# """, ('test@gmail.com',))
# user = cursor.fetchone()
# print("Користувач знайдений:", user)

# cursor.execute("""
#     UPDATE users SET name = %s WHERE email = %s
# """, ('Test2', 'test@gmail.com'))
# conn.commit()
# print("Ім'я користувача оновлено.")

# cursor.execute("""
#     DELETE FROM users WHERE email = %s
# """, ('test@gmail.com',))
# conn.commit()
# print("Користувач видалений.")

# cursor.close()
# conn.close()


from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["test_db"] 
users_collection = db["users"]

def create_user(name, email):
    user_data = {
        "name": name,
        "email": email,
        "created_at": datetime.now()
    }
    users_collection.insert_one(user_data)
    print("Користувач доданий:", user_data)

def get_user_by_email(email):
    user = users_collection.find_one({"email": email})
    if user:
        print("Користувач знайдений:", user)
    else:
        print("Користувача з таким email не знайдено.")
    return user

def update_user_name(email, new_name):
    result = users_collection.update_one(
        {"email": email},
        {"$set": {"name": new_name}}
    )
    if result.matched_count > 0:
        print("Ім'я користувача оновлено.")
    else:
        print("Користувача з таким email не знайдено.")

def delete_user_by_email(email):
    result = users_collection.delete_one({"email": email})
    if result.deleted_count > 0:
        print("Користувач видалений.")
    else:
        print("Користувача з таким email не знайдено.")

create_user("Test1", "test1@example.com")
get_user_by_email("test1@example.com")
update_user_name("test1@example.com", "Test1 Updated")
delete_user_by_email("test1@example.com")

client.close()

# Реляційні бази даних підходять для моделей, в яких важливі зв'язки між таблицями та структура. Дані бази даних потребують складної архітектури. Тобто спочатку потрібно продумати схему побудови таких баз даних. Вони мають розмір та тип даних, які містять. Нереляційні підходять для зберігання великої кількості даних, що зберігаються у вигляді ключ і значення, які можна швидко додавати, або масштабувати.