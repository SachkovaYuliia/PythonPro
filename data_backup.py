# Частина 3: (опціональне завдання)
# 1. Резервне копіювання:

# Налаштуйте резервне копіювання для бази даних (на прикладі MongoDB або Redis).
# 2. Моніторинг:

# Продемонструйте налаштування моніторингу продуктивності бази даних та аналізу запитів (наприклад, у MongoDB використовуйте MongoDB Compass для аналізу).import subprocess

import os
from pymongo import MongoClient
import subprocess
import redis
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.getenv("MONGO_URI") 
backup_directory_mongo = os.getenv("PATH")

redis_host = os.getenv("REDIS_HOST")
redis_port = int(os.getenv("REDIS_PORT"))
redis_cli_path = "redis-cli"  

def backup_mongodb():
    """Резервне копіювання MongoDB"""
    try:
        subprocess.run(["mongodump", "--uri", mongo_uri, "--out", backup_directory_mongo], check=True)
        print("Резервне копіювання MongoDB завершено.")
    except subprocess.CalledProcessError as e:
        print(f"Помилка резервного копіювання MongoDB: {e}")

def monitor_mongodb():
    """Моніторинг MongoDB"""
    client = MongoClient(mongo_uri)
    db = client.get_database()  

    server_status = db.command("serverStatus")
    print("Статистика сервера MongoDB:")
    print(server_status)

def backup_redis():
    """Резервне копіювання Redis"""
    try:
        subprocess.run([redis_cli_path, "save"], check=True)
        print("Резервне копіювання Redis завершено.")
    except subprocess.CalledProcessError as e:
        print(f"Помилка резервного копіювання Redis: {e}")

def monitor_redis():
    """Моніторинг Redis"""
    client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

    info = client.info()
    print("Статистика сервера Redis:")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    print("Резервне копіювання баз даних...")
    backup_mongodb()
    backup_redis()
    
    print("\n Моніторинг баз даних...")
    monitor_mongodb()
    monitor_redis()
