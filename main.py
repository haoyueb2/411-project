from flask import Flask, render_template, request, redirect, session
import db

app = Flask(__name__)
mydb = db.Database()
app.secret_key = "cs411"


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/search_user', methods=['POST'])
def search_user():
  firstName = request.form.get('fname')
  lastName = request.form.get('lname')
  email = request.form.get('email')
  result = mydb.search_user(firstName, lastName, email)
  return render_template('users.html', result=result)


@app.route('/call_procedure', methods=['POST'])
def call_procedure():
  result = mydb.call_procedure()
  return render_template('users.html', result=result)


@app.route('/add_user', methods=['POST'])
def add_new_user():
  if request.method == 'POST':
    firstName = request.form.get('fname1')
    lastName = request.form.get('lname1')
    email = request.form.get('email1')
    password = request.form.get('password1')
    print(password)
    mydb.add_user(firstName, lastName, email, password)
    return render_template('index.html')


@app.route('/add_unit', methods=['POST'])
def add_new_unit():
  if request.method == 'POST':
    buildingID = request.form.get('buildingid')
    conditioner = request.form.get('Conditioner')
    price = request.form.get('price')
    numberBedrooms = request.form.get('numBedroom')
    numberBathrooms = request.form.get('numBathroom')
    numberKitchens = request.form.get('numkitchen')
    totalLivingArea = request.form.get('totalLivingArea')
    mydb.add_unit(buildingID, conditioner, price, numberBedrooms,
                  numberBathrooms, numberKitchens, totalLivingArea)
    return render_template('login.html')


@app.route('/delete_user', methods=['POST'])
def delete_user():
  if request.method == 'POST':
    firstName = request.form.get('delete_firstname')
    lastName = request.form.get('delete_lastname')
    email = request.form.get('delete_email')
    mydb.delete_user(firstName, lastName, email)
    return render_template('login.html')


@app.route('/update_user', methods=['POST'])
def update_user():
  if request.method == 'POST':
    firstName = request.form.get('update_firstname')
    lastName = request.form.get('update_lastname')
    new_email = request.form.get('update_email')
    mydb.update_user(firstName, lastName, new_email)
    return render_template('login.html')


@app.route('/advance_1', methods=["POST"])
def get_advance_1():
  built_year = request.form.get('builtYear')
  stories = request.form.get('minStories')
  higher_lower = request.form.get('radio')
  result = mydb.advance_query_1(built_year, stories, higher_lower)
  return render_template('login.html',
                         built_year=built_year,
                         stories=stories,
                         higher_lower=higher_lower,
                         advance_1=result)


@app.route('/advance_2', methods=["POST"])
def get_advance_2():
  reviewYear = request.form.get('reviewYear')
  house_type = request.form.get('buildingType')
  air_condition = request.form.get('ac')
  result = mydb.advance_query_2(reviewYear, house_type, air_condition)

  return render_template('login.html',
                         reviewYear=reviewYear,
                         house_type=house_type,
                         air_condition=air_condition,
                         advance_2=result,
                         firstname=session['firstname'],
                         lastname=session['lastname'])


@app.route('/sim_disc_1', methods=["POST"])
def get_sim_disc_1():
  UnitID = request.form.get('UnitID')
  result = mydb.simple_discount_1(UnitID)

  return render_template('login.html', sim_disc_1=result)


@app.route('/login', methods=["POST"])
def login_user():
  email = request.form.get("login_email")
  password = request.form.get("login_password")
  result = mydb.login(email, password)
  firstname = None
  lastname = None
  if result:
    firstname = result[0]["FirstName"]
    lastname = result[0]["LastName"]
  session['firstname'] = firstname
  session['lastname'] = lastname
  return render_template('login.html', firstname=firstname, lastname=lastname)


@app.route('/test_db/')
def test_db():
  result = mydb.test()
  return result


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
