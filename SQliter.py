import sqlite3


class SQlite_db ():
    def __init__(self):
        """Подключение к БД"""

        self.connect = sqlite3.connect(r'main.db')
        self.cursor = self.connect.cursor()

        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS records(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                user_id INT NOT NULL,
                user_name VARCHAR(255) NOT NULL,
                url TEXT NOT NULL, 
                title TEXT NOT NULL,
                cur_episode INT NOT NULL,
                baner_url TEXT,
                date TEXT
                )""")
        self.connect.commit()

    def new_record(self, rec):
        """user_id , user_name, url, title, cur_episode, baner_url, date"""
        try:
            self.cursor.execute(
                'INSERT INTO records (user_id , user_name, url, title, cur_episode, baner_url, date) VALUES (?,?,?,?,?,?,?)', rec)
            self.connect.commit()
            print("Запись успешно сознанна!")
        except:
            print("Ошибка записи!")

    def get_all_records(self):
        try:
            self.cursor.execute('SELECT * FROM records')
            return self.cursor.fetchall()
        except:
            print("Ошибка возврата!")

    def get_user_records(self, user_id):
        try:
            self.cursor.execute(
                f'SELECT * FROM records WHERE user_id="{user_id}"')
            return self.cursor.fetchall()
        except:
            print('Ошибка поиска!')

    def del_by_id(self, id):
        try:
            self.cursor.execute(f'DELETE FROM records WHERE id = "{id}"')
            self.connect.commit()
        except:
            print("Ошибка удаления!")
