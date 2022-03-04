import sqlite3

async def startup (_):
    init_database()
    
    print('Бот онлаин!')


def init_database ():
    conn = sqlite3.connect(r'main.db')
    cur = conn.cursor()

    cur.execute("""
                CREATE TABLE IF NOT EXISTS records(
                id INT,
                user_id INT,
                user_name TEXT,
                url TEXT, 
                title TEXT,
                baner_url TEXT,
                date TEXT
                )""")
#  PRIMARY KEY
    conn.commit()

    # user = (1, 7006591, 'Test', 'https://', "test", 'https://', 'test')

    # cur.execute('INSERT INTO records VALUES(?,?,?,?,?,?,?)', user)

    # conn.commit()

    cur.execute("SELECT * FROM records")
    print (cur.fetchall())
    