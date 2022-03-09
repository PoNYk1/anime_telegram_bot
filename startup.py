
from SQliter import SQlite_db


async def startup(_):
    db = SQlite_db()

    print('Бот онлаин!')
