import psycopg2
from db_config import DB_CONFIG

# print(DB_CONFIG)

try:
    # conn = psycopg2.connect(**DB_CONFIG)
    conn = psycopg2.connect(
        host="34.29.153.67",
        database="people-museum:us-central1:db-museum-0603",
        user="postgres",
        password="admin"
    )
    print("Connected successfully!")
    conn.close()
except psycopg2.Error as e:
    print(f"Error: {e}")
