from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="fdsfoenoin"

db = MySQLConnector(app, 'mydb_janurary')

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect('/users/new')
    return render_template("index.html")

@app.route('/dashboard')
def go_to_dashboard():
        return render_template("dashboard.html")

@app.route('/users/new')
def new_user():
    return render_template("new_user.html")

@app.route('/users/create', methods=['POST'])
def create():
    errors = []
    if len(request.form['first_name']) < 2:
        errors.append('First name must be at least 2 characters long')

    if len(request.form['last_name']) < 2:
        errors.append('Last name must be at least 2 characters long')

    if len(request.form['password']) < 8:
        errors.append('Password must be at least 8 characters long')

    if request.form['password'] != request.form['confirm']:
        errors.append('Passwords do not match')

    if not EMAIL_REGEX.match(request.form['email']):
        errors.append("Email must be valid")
    
    if errors:
        for error in errors:
            flash(error)
        return redirect('/users/new')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # pw_hash = "jdsofdnewofin"
    print(pw_hash)

    print ("YAYY LOGGED IN")
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'pw_hash': pw_hash,
        'updated_at': datetime.now()
        }
    
    # query = "INSERT INTO USERS (first_name, last_name, email, pw_hash, updated_at) VALUES (" + data['first_name'], data['last_name'], data['email'], data['pw_hash'], "2019-01-19 17:19:12"
    # query = 'SELECT * FROM  locations;'
    # query = "INSERT INTO USERS (first_name, last_name, email, pw_hash, updated_at) VALUES (%s);" % (data['first_name'], data['last_name'], data['email'], data['pw_hash'], "2019-01-19 17:19:12")
    columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    # values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    values = ''.join(str(x) for x in data.values())
    # values = data.values()
    query = "INSERT INTO %s (%s) VALUES (%s);" % ("USERS", columns, values)
    # USERS (first_name, last_name, email, pw_hash, updated_at) VALUES (%%(first_name)s, %%(last_name)s, %%(email)s, %%(pw_hash)s, now());"
 
    user_id = db.query_db(query)
    session['user_id'] = user_id

    print("**************")
    print (user_id)

    return redirect('/')
# @app.route('/login', methods=['POST'])
# def login():
#     pass


# mysql = MySQLConnector(app, 'mydb_janurary')
# print (mysql.query_db("SELECT * FROM locations"))
if __name__ == "__main__":
    app.run(debug=True)


