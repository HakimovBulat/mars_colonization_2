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

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=2)
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')