from flask import Flask, render_template#загружаем библиотеку FLask
from api.sql_master import SQLiteMaster#загружаем библиотеку SQLiteMaster

app = Flask(__name__)
app.debug = True #включаем онлайн тест
sql_api = SQLiteMaster() #создаем переменную sql_api
choose = sql_api.get_data_DoS() #создаем переменную choose


@app.route('/') # указываем ссылку на страницу
def index():
    return render_template('index.html',
                           title="Список направлений",
                           choose=choose)#отправляем список данных choose в index.html для дальнейшей работы с ней

@app.route('/1') # указываем ссылку на страницу
def course1():
    data = sql_api.get_data("Courses",choose[0][0])#выбираем курсы опеределенного направления в нашем случае 1 Информатика и вычислительная техника
    return render_template('Course2.html',
                           title=choose[0][1],
                           data=data)#отправляем список данных data в Course2.html для дальнейшей работы с ней
@app.route('/2') # указываем ссылку на страницу
def course2():
    data = sql_api.get_data("Courses",choose[1][0])
    return render_template('Course2.html',
                           title=choose[1][1],
                           data=data)
@app.route('/3') # указываем ссылку на страницу
def course3():
    data = sql_api.get_data("Courses",choose[2][0])
    return render_template('Course2.html',
                           title=choose[2][1],
                           data=data)

if __name__ == '__main__':
    app.run()
