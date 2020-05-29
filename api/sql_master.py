import sqlite3
import os

class SQLiteMaster:
    def __init__(self):
        db_path = os.path.dirname(os.path.abspath(__file__)) + '/test.db'
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def get_data(self,table,target):#данные из courses
        sql = f"select * from {table} where DoS_code={target}"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_data_DoS(self):  # данные из courses
        sql = f"select * from direction_of_study"
        self.cursor.execute(sql)
        return self.cursor.fetchall()


if __name__=="__main__": #тестируем
    sql_api = SQLiteMaster()
    otvet=sql_api.get_data("Courses",3)
    otvet1=sql_api.get_data_DoS()
    [print(govn) for govn in otvet]
    print (otvet1[1][1])

