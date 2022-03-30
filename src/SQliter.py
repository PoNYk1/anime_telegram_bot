import sqlite3
import datetime


class SQLiter_BD ():

    def __init__(self, user_id):
        self.connect = sqlite3.connect("main.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS anime_list(
                    key INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    url TEXT NOT NULL,
                    title TEXT NOT NULL,
                    cur_episode INT NOT NULL,
                    baner_url TEXT,
                    last_update_date TEXT NOT NULL,
                    new_epesode INT NOT NULL
                )""")
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    key INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INT NOT NULL
                )
                            """)
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS sub (
                    key INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INT NOT NULL,
                    anime_key INT NOT NULL
                )
                            """)

        self.connect.commit()

        self.cur_user = self.__check_user(user_id)

    def close(self):
        self.connect.close()
        print(
            f'[{self.cur_user}]: Соединение закрыто...'
        )

# =====================================

    def __check_user(self, user_id):
        self.cursor.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
        user = self.cursor.fetchone()

        if user == None:
            self.cursor.execute(
                f'INSERT INTO users (user_id) VALUES ({user_id})')
            print(f"Новый пользователь: {user_id}")
            self.connect.commit()
        return user_id

    def __check_anime(self, anime):
        self.cursor.execute(
            f'SELECT * FROM anime_list WHERE title = "{anime[1]}"')
        ani_title = self.cursor.fetchone()
        if ani_title == None:
            date = datetime.datetime.now().date()
            self.cursor.execute(
                f'INSERT INTO anime_list (url, title, cur_episode, baner_url, last_update_date, new_epesode) VALUES (?,?,?,?,?,?)',
                (*anime, date, 0)
            )
            self.connect.commit()
            print(f'[{self.cur_user}]: Новое аниме в списке - {anime[1]}')

# =====================================

    def new_sub(self, anime_info):
        """ url, title, cur_episode, baner_url"""

        self.__check_anime(anime_info)

        self.cursor.execute(
            f'SELECT * FROM anime_list WHERE title = "{anime_info[1]}"'
        )
        cur_anime = self.cursor.fetchone()

        self.cursor.execute(
            f'SELECT * FROM sub WHERE user_id = "{self.cur_user}" AND anime_key = "{cur_anime[0]}"'
        )
        sub_rez = self.cursor.fetchone()

        if sub_rez == None:
            self.cursor.execute(
                'INSERT INTO sub (user_id, anime_key) VALUES (?,?)', (
                    self.cur_user, cur_anime[0])
            )
            self.connect.commit()
            print(f'[{self.cur_user}]: оформленна подписка на - {cur_anime[2]}')

    def del_sub(self, key):
        self.cursor.execute(
            f'SELECT * FROM sub WHERE key="{key}" AND user_id="{self.cur_user}"'
        )
        key_rez = self.cursor.fetchone()

        if key_rez != None:
            self.cursor.execute(
                f'DELETE FROM sub WHERE key="{key}" AND user_id="{self.cur_user}"'
            )
            self.connect.commit()
            return True
        else:
            return False

    def get_user_sub(self):
        self.cursor.execute(
            f'SELECT * FROM sub WHERE user_id = "{self.cur_user}"'
        )
        user_sub_arr = self.cursor.fetchall()

        return user_sub_arr

    def get_user_sub_anime(self):
        self.cursor.execute(
            f'SELECT * FROM sub WHERE user_id = "{self.cur_user}"'
        )
        user_sub_arr = self.cursor.fetchall()

        anime_list = []
        for sub in user_sub_arr:
            self.cursor.execute(
                f'SELECT * FROM anime_list WHERE key = "{sub[2]}"'
            )
            anime_list = [*anime_list, self.cursor.fetchone()]

        return anime_list

    def get_anime_list(self):
        self.cursor.execute(
            'SELECT * FROM anime_list'
        )

        rezult = self.cursor.fetchall()

        return rezult

    def get_anime_list(self):
        self.cursor.execute(
            'SELECT * FROM anime_list'
        )

        rezult = self.cursor.fetchall()

        return rezult

    def update_episode(self, key, new_epesode):
        self.cursor.execute(
            f'SELECT * FROM anime_list WHERE key = "{key}"'
        )
        key_rez = self.cursor.fetchone()

        if key_rez != None:
            date = datetime.datetime.now().date()
            self.cursor.execute(
                f'UPDATE anime_list SET cur_episode = "{new_epesode}", last_update_date = "{date}", new_epesode = "1"  WHERE key = "{key}"'
            )
            self.connect.commit()
            print(f'{key_rez[2]} - Обновлен эпизод на {new_epesode}')
            return True
        else:
            return False

    def check_anime_list_status(self):
        anime_list = self.get_anime_list()
        date = datetime.datetime.now().date()

        for anime in anime_list:
            if anime[5] != str(date) and anime[6] == 1:
                self.cursor.execute(
                    f'UPDATE anime_list SET new_epesode = "0"  WHERE key = "{anime[0]}"'
                )
                self.connect.commit()

                print(f'Аниме {anime[2]} - изменен статус на 0')


class SQLiter():
    def __init__(self, user_id):
        self.user_id = user_id
        self.sqliter = None

    def __enter__(self):
        self.sqliter = SQLiter_BD(self.user_id)

        return self.sqliter

    def __exit__(self, a, e, i):
        if self.sqliter:
            self.sqliter.close()
