from flask import Flask, render_template
import db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/insert')
def insert():
    return render_template('')


@app.route('/test_db/')
def test_db():
    mydb = db.Database()
    result = mydb.test()
    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
