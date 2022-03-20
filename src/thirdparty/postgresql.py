import psycopg2

class db:
    def __init__(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="flask_db",
            user="user",
            password="")

    def drop_table(self, table_name):
        cur = self.connection.cursor()
        cur.execute(f'DROP TABLE IF EXISTS {table_name};')
        self.connection.commit()
        cur.close()

    #쿼리가 문자열이 아닌 경우 예외
    def create_table(self, table_name, query):
        cur = self.connection.cursor()
        cur.execute(f'CREATE TABLE {table_name} ({query});')
        self.connection.commit()
        cur.close()

    # 문자열에 작음 따옴표 필요
    # 쿼리 만드는 메소드 추가 필요(다른 클래스에)
    def insert(self, table_name, record):
        cur = self.connection.cursor()
        cur.execute(f'INSERT INTO {table_name} ({", ".join(record.keys())}) VALUES ({", ".join(record.values())});')
        self.connection.commit()
        cur.close()

    def select(self, table_name):
        cur = self.connection.cursor()
        cur.execute(f'SELECT * FROM {table_name};')
        rows = cur.fetchall()
        cur.close()
        return rows;

    def close(self):
        self.connection.close()
