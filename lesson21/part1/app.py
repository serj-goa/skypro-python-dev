from flask import Flask, render_template
from json import load


app = Flask(__name__)


def get_courses():
    with open('data/courses.json', 'r') as fd:
        return load(fd)


@app.route('/users/<int:id>')
def users(id):
    courses = get_courses()
    return render_template('users/show.html', courses=courses, id=id)


@app.route('/courses/')
def courses():
    courses = get_courses()
    return render_template('courses/index.html', courses=courses)


if __name__ == '__main__':
    app.run(debug=True)
