from flask import Flask, render_template, request


app = Flask(__name__)

all_users = ['mike', 'mishel', 'adel', 'keks', 'kamila']


@app.route('/users/')
def filtered_users():
    term = request.args.get('term')

    if not term:
        term = ''

    users = filter(lambda x: term in x, all_users)
    return render_template('users/index.html', users=users, search=term)


if __name__ == '__main__':
    app.run(debug=True)
