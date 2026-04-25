import psycopg2

# Make sure this name is EXACTLY get_db_connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="cricbuzz_db",
            user="souravsamanta", 
            password="", 
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None