import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

DB_NAME = "myproject_db"
DB_USER = "myproject_user"
DB_PASSWORD = "password"

def create_database():
    try:
        con = psycopg2.connect(dbname='postgres', user='postgres', password='postgres', host='localhost')
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()

        cur.execute(f"SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'")
        if not cur.fetchone():
            cur.execute(f"CREATE DATABASE {DB_NAME}")

        cur.execute(f"SELECT 1 FROM pg_roles WHERE rolname = '{DB_USER}'")
        if not cur.fetchone():
            cur.execute(f"CREATE USER {DB_USER} WITH PASSWORD '{DB_PASSWORD}'")

        cur.execute(f"GRANT ALL PRIVILEGES ON DATABASE {DB_NAME} TO {DB_USER}")

        cur.close()
        con.close()
        print("Database and user are ready.")
    except Exception as e:
        print("Error:", e)

if __name__ == '__main__':
    create_database()
