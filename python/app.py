from flask import Flask, render_template, request, send_file
import os
from api.sql_master import SQLiteMaster
from api.excel import save_courses_to_excel

app = Flask(__name__)
app.debug = True #включаем онлайн тест
sql_api = SQLiteMaster()
# sml_save = SaveDoS_Table()
choose = sql_api.get_data_DoS() #создаем переменную choose в которой храним названия всех направлений

@app.route('/')
def index():
      return render_template('index.html',
                           title='Список направлений',
                           choose=choose)#Выводим названия всех направлений из БД


@app.route('/get-course', methods=['GET'])
def get_course():
    if request.method == 'GET':
        course_id = request.args.get('id')#Из запроса вытаскиваем аргумент id
        result = sql_api.get_data("Courses",int(course_id))#Вытаскиваем данные из таблицы по заданному id
        return {'result': result}#Отвечам на запрос(Результат GET запроса)

@app.route('/save_excel_course', methods=['POST'])
def save_course():
    if request.method == 'POST':
        json_data = request.get_json()
        courselist = json_data.get('list',[''])
        courselist = ','.join(courselist)
        result = sql_api.get_data_file("Courses",courselist)
        save_courses_to_excel(result)
        return send_file(os.path.abspath(os.path.dirname(os.path.abspath(__file__)))+'\\tmp.xlsx', attachment_filename='tmp.xlsx')


if __name__ == '__main__':
    app.run()
