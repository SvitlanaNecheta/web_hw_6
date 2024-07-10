import psycopg2
from contextlib import contextmanager

database='./test.db'

@contextmanager
def create_conection():
    conn = None
    try:
        print("Trying to connect to the database...")
        conn = psycopg2.connect(
        
            database="test",
            user="postgres",
            password="s4v0e1t6a",
            
        )
        print("Connection successful.")
        yield conn
    except psycopg2.OperationalError as err:
        print("OperationalError encountered.")
        raise RuntimeError(f"Failed to create DB connection: {err}")
    except UnicodeDecodeError as err:
        print("UnicodeDecodeError encountered.")
        raise RuntimeError(f"Unicode decoding error: {err}")
    except Exception as err:
        print("An unexpected error encountered.")
        raise RuntimeError(f"An unexpected error occurred: {err}")
    finally:
        if conn:
            print("Closing the connection.")
            conn.close()
        else:
            print("Connection was not established.")

# Example usage
try:
    with create_conection() as conn:
        print("Performing database operations...")
        # Place your database operations here
except RuntimeError as e:
    print(e)
