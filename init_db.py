import sqlite3
from sqlite3 import Error as DBError

def create_db(db_file, table_sql):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        c = conn.cursor()
        c.execute(table_sql)
    except DBError as e:
        print(e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    table_sql = '''CREATE TABLE golems(
                        id integer PRIMARY KEY,
                        name text NOT NULL,
                        type text NOT NULL,
                        config blob
                    );'''
    create_db('golems.db', table_sql)

