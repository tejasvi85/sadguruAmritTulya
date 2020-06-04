import sqlite3


def createDatabase():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    create_table = """CREATE TABLE IF NOT EXISTS items
                        (name varchar(100), description varchar(100),
                        price float, filename varchar(100), photo blob, 
                        PRIMARY KEY (name));"""
    cur.execute(create_table)
    conn.commit()
    conn.close()


def selectqueryfunc(select_query, inputtuple=()):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    cur.execute(select_query, inputtuple)
    result = cur.fetchall()
    conn.close()
    return result


def insertqueryfunc(insert_query, inputtuple):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    cur.execute(insert_query, inputtuple)
    conn.commit()
    conn.close()


def deletequeryfunc(delete_query, inputtuple):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()

    cur.execute(delete_query, inputtuple)
    conn.commit()
    conn.close()


def allowed_file(filename, ALLOWED_EXTENSIONS):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
