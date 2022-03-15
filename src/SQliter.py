import sqlite3
from src.SQL_code import create_records_table, create_user_table


class SQlite_db ():
    def __init__(self, user_id, user_name):
        """Подключение к БД"""

        self.connect = sqlite3.connect(r'main.db')
        self.cursor = self.connect.cursor()

        self.cursor.execute(create_records_table)
        self.cursor.execute(create_user_table)
        self.connect.commit()

        self.cur_user = self.__check_user(user_id, user_name)

    def __check_user(self, user_id, user_name):
        self.cursor.execute(
            f'SELECT * FROM users WHERE user_id = "{user_id}"')

        if len(self.cursor.fetchall()) == 0:
            self.cursor.execute(
                f'INSERT INTO users (user_id , user_name) VALUES (?,?)', (user_id, user_name))
            self.connect.commit()
        return user_id

    def new_record(self, rec):
        """ url, title, cur_episode, baner_url, date"""
        print(rec)
        try:
            self.cursor.execute(
                'INSERT INTO records (user_id , url, title, cur_episode, baner_url, date) VALUES (?,?,?,?,?,?)', (self.cur_user, *rec))
            self.connect.commit()
            print("Запись успешно сознанна!")
        except:
            print("Ошибка записи!")

    # def get_all_records(self):
    #     try:
    #         self.cursor.execute('SELECT * FROM records')
    #         return self.cursor.fetchall()
    #     except:
    #         print("Ошибка возврата!")

    def get_user_records(self):
        try:
            self.cursor.execute(
                f'SELECT * FROM records WHERE user_id="{self.cur_user}"')
            return self.cursor.fetchall()
        except:
            print('Ошибка поиска!')

    def del_by_id(self, id):
        try:
            self.cursor.execute(f'DELETE FROM records WHERE id = "{id}"')
            self.connect.commit()
        except:
            print("Ошибка удаления!")
