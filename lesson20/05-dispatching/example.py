from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return 'Hello from POST /users'
    return 'Hello from GET /users'


if __name__ == '__main__':
    app.run()
