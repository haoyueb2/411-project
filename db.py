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
    db = "testDB"
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

  def search_user(self, firstName, lastName, email):
    sql = "select * from testDB.User where FirstName = %s or LastName = %s or Email = %s"
    self.cur.execute(sql, (firstName, lastName, email))
    result = self.cur.fetchall()
    return result

  def add_user(self, firstName, lastName, email, password):
    try:
      sql = "INSERT INTO testDB.User (FirstName, LastName, Email, Password) VALUES (%s, %s, %s, %s)"
      self.cur.execute(sql, (firstName, lastName, email, password))
      self.con.commit()
    except:
      print("error!")

  def add_unit(self, buildingID, conditioner, price, numberBedrooms, numberBathrooms, numberKitchens, totalLivingArea):
      sql = "INSERT INTO testDB.Unit (BuildingID, Conditioner, Price, NumberBedrooms, NumberBathrooms, NumberKitchens, TotalLivingArea) VALUES (%s, %s, %s, %s, %s, %s, %s)"
      self.cur.execute(sql, (buildingID, conditioner, price, numberBedrooms,
                             numberBathrooms, numberKitchens, totalLivingArea))
      self.con.commit()
    
  def delete_user(self, firstName, lastName, email):
    sql = "DELETE FROM testDB.User WHERE Email = %s AND FirstName = %s AND LastName = %s"
    self.cur.execute(sql, (email, firstName, lastName))
    self.con.commit()

  def update_user(self, firstName, lastName, email):
    sql = "UPDATE testDB.User SET Email = %s WHERE FirstName = %s AND LastName = %s"
    self.cur.execute(sql, (email, firstName, lastName))
    self.con.commit()

  def advance_query_1(self, built_year, stories, higher_lower):
    sql = ''
    stories = int(stories)
    if higher_lower == "lower":
      sql = "SELECT b.BuildingID, YearsBuilt, TotalStories, Price FROM testDB.Building b Join testDB.Unit USING(BuildingID) WHERE Price < (SELECT AVG(Price) FROM testDB.Unit) AND YearsBuilt > %s AND TotalStories >= %s LIMIT 15"
    else:
      sql = "SELECT b.BuildingID, YearsBuilt, TotalStories, Price FROM testDB.Building b Join testDB.Unit USING(BuildingID) WHERE Price > (SELECT AVG(Price) FROM testDB.Unit) AND YearsBuilt > %s AND TotalStories >= %s LIMIT 15"
    self.cur.execute(sql, (built_year, stories))
    self.con.commit()
    result = self.cur.fetchall()
    return result

  def advance_query_2(self, reviewYear, house_type, air_condition):

    if air_condition == "on":
      air_condition = 1
    else:
      air_condition = 0

    sql = "SELECT b.BuildingID, Rating, COUNT(Rating) Number_Rating FROM testDB.Building b JOIN testDB.Review USING(BuildingID) WHERE ReviewDate LIKE %s AND BuildingType = %s AND AirConditioning = %s GROUP BY BuildingID, Rating ORDER BY Number_Rating DESC LIMIT 15"
    reviewYear = reviewYear + "%"
    self.cur.execute(sql, (reviewYear, house_type, air_condition))
    self.con.commit()
    result = self.cur.fetchall()
    return result

  def simple_discount_1(self, UnitID):
    sql = "SELECT * FROM testDB.DiscountTable WHERE UnitID = %s"
    self.cur.execute(sql, (UnitID))
    self.con.commit()
    result = self.cur.fetchall()
    return result

  def call_procedure(self):
    sql = "call testDB.air_discount()"
    self.cur.execute(sql)
    self.con.commit()
    result = self.cur.fetchall()
    return result

  def login(self, email, password):
    sql = "SELECT FirstName, LastName FROM testDB.User WHERE Email = %s and Password = %s"
    self.cur.execute(sql, (email, password))
    self.con.commit()
    result = self.cur.fetchall()
    return result


# if __name__ == '__main__':
#     app.run(debug=True)
