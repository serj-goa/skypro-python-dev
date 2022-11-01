from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    # Получить доступ к содержимому запроса можно через специальный объект request
    if request.method == 'POST':
        return 'Hello, POST!'

    return 'Hello, GET!'


@app.get('/')
def hello_get():
    return 'Hello, GET!'


@app.post('/')
def hello_post():
    return 'Hello, POST!'


if __name__ == '__main__':
    app.run()
