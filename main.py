from flask import Flask, render_template

app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')