from flask import Flask
import pymysql
# from flask_cors import *
# from flask import Response,request

app = Flask(__name__)
# CORS(app, supports_credentials=True)


class Database:

  def __init__(self):
    host = "34.171.35.27"
    user = "root"
    password = "test1234"
    db = "cs-411"
    self.con = pymysql.connect(host=host,
                               user=user,
                               password=password,
                               db=db,
                               cursorclass=pymysql.cursors.DictCursor)
    self.cur = self.con.cursor()

  def test(self):
    sql = "select * from testDB.Unit"
    self.cur.execute(sql)
    result = self.cur.fetchall()
    return result


# if __name__ == '__main__':
#     app.run(debug=True)
