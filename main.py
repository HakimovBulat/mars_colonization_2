from flask import Flask, render_template, redirect
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
@app.route('/index/<title>')
def index(title='Приветствие'):
    return render_template('base.html', title=title)


@app.route('/training')
@app.route('/training/<prof>')
def training(prof=''):
    return render_template('training.html', prof=prof)


@app.route('/list_prof/<list>')
def list_prof(list):
    items = ['Врач', 'Метеоролог', 'Строитель', 'Инженер', 'Пилот', 'Диспетчер дронов', 'Штурман']
    return render_template('list_prof.html', list=list, items=items)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {
        'title' : 'Анкета', 
        'surname' : 'Хакимов', 
        'name' : 'Булат', 
        'education' : 'Среднее общее', 
        'profession' : 'Программист', 
        'sex' : 'male', 
        'motivation' : 'Я люблю красные штуки', 
        'ready' : 'True'
    }
    return render_template('auto_answer.html', **params)


@app.route('/distribution')
def distribution():
    ausrtonauts = ['Стивен Спилберг', "Джордж Лукас", "Ридли Скотт", "Кристофер Нолан", "Дени Вильнёв"]
    return render_template('distribution.html', ausrtonauts=ausrtonauts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


@app.route('/success')
def success():
    return render_template('success.html', title='Доступ разрешён')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')