import sqlite3
from src.SQL_code import create_records_table, create_user_table


class SQlite_db ():
    def __init__(self):
        """Подключение к БД"""

        self.connect = sqlite3.connect(r'main.db')
        self.cursor = self.connect.cursor()

        self.cursor.execute(create_records_table)
        self.cursor.execute(create_user_table)
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
