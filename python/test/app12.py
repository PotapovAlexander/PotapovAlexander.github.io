from flask import Flask, render_template, request
from api.sql_master import SQLiteMaster

app = Flask(__name__)
sql_api = SQLiteMaster()


@app.route('/')
def index():
    choose = [
        [0, 'SAMPLE TEXT'],
        [1, 'BLAZE IT']
    ]
    return render_template('index.html',
                           title='Roflan Ebalo',
                           choose=choose)


@app.route('/get-course', methods=['GET'])
def get_course():
    if request.method == 'GET':
        course_id = request.args.get('id')
        course1 = [
            [0, 'lmao', 'kek'],
            [1, 'dark souls', 'govno']
        ]
        course2 = [
            [0, 'roflan', 'pomoyka'],
            [1, 'ah ti suka', 'nikto ne smeet govorit 4to ds govno']
        ]
        result = [course1, course2]
        return {'result': result[int(course_id)]}


if __name__ == '__main__':
    app.run()
