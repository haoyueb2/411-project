from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = '34.171.35.27'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'test1234'
app.config['MYSQL_DB'] = 'CS-411'

mysql = MySQL(app)



@app.route('/')
def index():
    return 'Hello from Flask!'


app.run(host='0.0.0.0', port=81)
