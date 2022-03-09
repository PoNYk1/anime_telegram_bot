create_records_table = """
                CREATE TABLE IF NOT EXISTS records(
                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  user_id INT NOT NULL,
                  user_name VARCHAR(255) NOT NULL,
                  url TEXT NOT NULL,
                  title TEXT NOT NULL,
                  cur_episode INT NOT NULL,
                  baner_url TEXT,
                  date TEXT
                )"""

create_user_table = """
                CREATE TABLE IF NOT EXISTS users(
                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  user_id INT NOT NULL,
                  user_name VARCHAR(255) NOT NULL
                )
"""
