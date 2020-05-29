from flask import Flask, render_template
from api.sql_master import SQLiteMaster

app = Flask(__name__)
app.debug = True #включаем онлайн тест
sql_api = SQLiteMaster()
choose = sql_api.get_data_DoS()


@app.route('/') # указываем ссылку на страницу
def index():
    return render_template('index.html',
                           title="Список направлений",
                           choose=choose)

@app.route('/1') # указываем ссылку на страницу
def course1():
    # print(choose[0])
    data = sql_api.get_data("Courses",choose[0][0])
    return render_template('Course2.html',
                           title=choose[0][1],
                           data=data)
@app.route('/2') # указываем ссылку на страницу
def course2():
    print(choose[1])
    data = sql_api.get_data("Courses",choose[1][0])
    return render_template('Course2.html',
                           title=choose[1][1],
                           data=data)
@app.route('/3') # указываем ссылку на страницу
def course3():
    print(choose[2])
    data = sql_api.get_data("Courses",choose[2][0])
    return render_template('Course2.html',
                           title=choose[2][1],
                           data=data)

if __name__ == '__main__':
    app.run()
