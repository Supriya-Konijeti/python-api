from psycopg2.extras import RealDictCursor
import psycopg2


def insert_into(new_todo):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Priyak@33",
        port="5432"
    )
    print(conn)
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Todo(ID, Name, Company)
            VALUES (%s, %s, %s)''', (new_todo.get("id"), new_todo.get('name'), new_todo.get('company')))
    """cursor.execute(
        "insert into Todo(id,name,company) values( %s,%s,%s)", (new_todo.get("id"), new_todo.get("name"), new_todo.get("company")))
    """
    conn.commit()

    conn.close()


def get_all():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Priyak@33",
        port="5432"
    )
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute('''SELECT * FROM Todo;''')
    return cur.fetchall()
