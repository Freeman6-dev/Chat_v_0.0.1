from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable
from config import USER, PASSWORD, HOST


def create_db():
    # while True:
    try:
        cnx = connect(user=USER, password=PASSWORD, host=HOST)
        cnx.autocommit = True
        print("Succes")
        # good = False
        # while True:

        try:
            # while not good:
            db = input("Database name: ")
            cursor = cnx.cursor()
            sql = f'CREATE DATABASE {db};'
            cursor.execute(sql)
            cursor.close()
            print("Database created!")
            # good = True
        # break
        except DuplicateDatabase:
            print("Error: this name of db is in use!")
        cnx.close()

    except OperationalError:
        print("Error: check user name or/and password!")



if __name__ == '__main__':
    create_db()
