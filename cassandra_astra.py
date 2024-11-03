# Варіант 3: Cassandra (колонкова база даних)
# 1. Зберігання логів подій:

# Створіть таблицю для зберігання логів подій у Cassandra. Логи можуть містити поля: event_id, user_id, event_type, timestamp, metadata.
# 2. CRUD операції:

# Create: Додайте новий лог події до таблиці.
# Read: Отримайте всі події певного типу за останні 24 години.
# Update: Оновіть додаткову інформацію в полі metadata для певного event_id.
# Delete: Видаліть старі події (старші за 7 днів) з бази даних.

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from dotenv import load_dotenv
from datetime import datetime, timedelta
import os
import uuid

load_dotenv()

client_id = os.getenv("ASTRA_CLIENT_ID")
client_secret = os.getenv("ASTRA_CLIENT_SECRET")
secure_connect_bundle_path = os.getenv("SECURE_CONNECT_BUNDLE_PATH")

cloud_config = {
    'secure_connect_bundle': secure_connect_bundle_path
}
auth_provider = PlainTextAuthProvider(client_id, client_secret)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

session.execute("""
    CREATE KEYSPACE IF NOT EXISTS event_logs 
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1}
""")
session.set_keyspace("event_logs")

session.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        event_id UUID PRIMARY KEY,
        user_id UUID,
        event_type text,
        timestamp timestamp,
        metadata map<text, text>
    )
""")

def create_event_log(user_id, event_type, metadata):
    event_id = uuid.uuid4()
    session.execute("""
        INSERT INTO logs (event_id, user_id, event_type, timestamp, metadata)
        VALUES (%s, %s, %s, %s, %s)
    """, (event_id, user_id, event_type, datetime.now(), metadata))
    print(f"Лог події {event_id} додано.")

def get_events_by_type(event_type):
    one_day_ago = datetime.now() - timedelta(days=1)
    rows = session.execute("""
        SELECT * FROM logs WHERE event_type = %s AND timestamp >= %s ALLOW FILTERING
    """, (event_type, one_day_ago))
    for row in rows:
        print(row)

def update_event_metadata(event_id, new_metadata):
    session.execute("""
        UPDATE logs SET metadata = %s WHERE event_id = %s
    """, (new_metadata, event_id))
    print(f"Метадані для події {event_id} оновлено.")

def delete_old_events():
    seven_days_ago = datetime.now() - timedelta(days=7)
    session.execute("""
        DELETE FROM logs WHERE timestamp < %s ALLOW FILTERING
    """, (seven_days_ago,))
    print("Старі події видалено.")

def close_connection():
    session.shutdown()
    cluster.shutdown() 
    print("Підключення до Cassandra закрито.")

create_event_log(user_id=uuid.uuid4(), event_type="login", metadata={"location": "Kyiv", "device": "Mobile"})
get_events_by_type("login")
update_event_metadata(event_id=uuid.uuid4(), new_metadata={"location": "Lviv"})
delete_old_events()

close_connection()
