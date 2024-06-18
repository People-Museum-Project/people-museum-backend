import sqlalchemy

def create_tables(db):
    """
    Creates the necessary tables in the database.

    Args:
        db (sqlalchemy.engine.base.Engine): The database connection object.
    """
    try:
        with db.connect() as conn:
            conn.execute(sqlalchemy.text("""
                CREATE TABLE IF NOT EXISTS "Person" (
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
            """))
            print("Table Person created or already exists.")

            conn.execute(sqlalchemy.text("""
                CREATE TABLE IF NOT EXISTS "PeopleCollection" (
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
            """))
            print("Table PeopleCollection created or already exists.")
    except Exception as e:
        print(f"An error occurred while creating tables: {e}")
