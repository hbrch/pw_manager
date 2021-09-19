import sqlite3

#DB creation
def database():
    with sqlite3.connect('****.****') as db:
        c = db.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS masterpassword(
    id INTEGER PRIMARY KEY,
    password TEXT NOT NULL);
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS vault(
    id INTEGER PRIMARY KEY,
    website TEXT NOT NULL,
    password TEXT NOT NULL);
    """)