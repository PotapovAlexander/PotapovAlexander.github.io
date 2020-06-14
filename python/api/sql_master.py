import sqlite3 #загружаем библиотеку sqlite 3
import os #загружаем библиотеку os

class SQLiteMaster:#Создаем class SQLiteMaster для взаимодействия с нашей базой данных test.db
    def __init__(self):
        db_path = os.path.dirname(os.path.abspath(__file__)) + '/test.db'#Задаем путь к базе данных
        self.conn = sqlite3.connect(db_path, check_same_thread=False)#Соединяемся к файлу с базой данных
        self.cursor = self.conn.cursor()

    def get_data(self,table,target):#выгружаем данные из courses в get_data
        answer = [["ID","Курс","Часы","Стоимость","Тип","Форма сдачи"]]
        sql = f"select Courses_id,Course_name,Course_hours,Course_value,Course_type,Course_typeX from {table} where DoS_code={target}"
        self.cursor.execute(sql)
        answer+=self.cursor.fetchall()
        return answer

    def get_data_file(self,table,target):#выгружаем данные из courses в get_data
        answer = []
        sql = f"select Course_name,Course_hours,Course_value,Course_type,Course_typeX from {table} where Courses_id in ({target})"
        print(sql)
        self.cursor.execute(sql)
        answer+=self.cursor.fetchall()
        return answer

    def get_data_DoS(self):  #выгружаем данные из direction_of_study в get_data_DoS
        sql = f"select Dos_code, DoS_name from direction_of_study"
        self.cursor.execute(sql)#
        return self.cursor.fetchall()#


if __name__=="__main__": #тестируем
    sql_api = SQLiteMaster()
    ids=['1','2','3']
    ids = ','.join(ids)
    otvet=sql_api.get_data_file("Courses",ids)
    [print(govn) for govn in otvet]


