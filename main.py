from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<H2>Hello world</H2><br><a href='/index'>goes to second page</a>"   # создает референсную ссылку на вторую страницу

@app.route('/index/<x>/<y>')
def index2(x, y):
    return f'Результат: {int(x) + int(y)}'


if __name__ == '__main__':
    app.run()


