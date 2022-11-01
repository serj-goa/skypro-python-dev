from flask import Flask


app = Flask(__name__)


@app.post('/users')
def users():
    return 'Users', 302


if __name__ == '__main__':
    app.run()
