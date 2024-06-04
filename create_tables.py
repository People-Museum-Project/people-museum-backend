import psycopg2
from db_config import DB_CONFIG

def create_tables():
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Person (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        image VARCHAR(255),
        description TEXT,
        bio_docs TEXT[],
        authored_docs TEXT[],
        collections INTEGER[],
        owner INTEGER,
        share_list INTEGER[],
        is_public BOOLEAN DEFAULT FALSE
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS PeopleCollection (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        image VARCHAR(255),
        description TEXT,
        bio_docs TEXT[],
        people INTEGER[],
        owner INTEGER,
        share_list INTEGER[],
        is_public BOOLEAN DEFAULT FALSE
    );
    """)

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_tables()