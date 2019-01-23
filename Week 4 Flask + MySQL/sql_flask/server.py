from flask import Flask, render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector
import re
from datetime import datetime
from helpers import users, locations


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="fdsfoenoin"

db = MySQLConnector(app, 'mydb_janurary')

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect('/users/new')
    # user = users.get_current_user(session['user_id'])
    return render_template("index.html")
    # user=users.get_current_user(session['user_id']), 
    # locations = locations.get_all_locations()),
    # activities = actitivies.get_all_for_current_user(session['user_id'])

@app.route('/dashboard')
def go_to_dashboard():
        return render_template("dashboard.html")

@app.route('/users/new')
def new_user():
    return render_template("new_user.html")

@app.route('/users/create', methods=['POST'])
def create():
    errors = users.validate(request.form)
    if errors:
        for error in errors:
            flash(error)
        return redirect('/users/new')
    user_id = users.create(request.form, bcrypt)
    session['user_id'] = user_id
    print("**************")
    print (user_id)
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    response = users.check_login(request.form, bcrypt)
    if response:
        session['user_id'] = response
        return redirect('/dashboard')
    else:
        for error in response:
            flash(error)
        return redirect('index.html')
    print("**************")


    # valid, response = users.check_login(request.form, bcrypt)
    # if valid:
    #     session['user_id'] = response
    #     return redirect('/')
    # else:
    #     for error in response:
    #         flash(error)
    #     return redirect('index.html')
    # print("**************")
    # return redirect("/users/new")

if __name__ == "__main__":
    app.run(debug=True)



# mysql = MySQLConnector(app, 'mydb_janurary')
# print (mysql.query_db("SELECT * FROM locations"))

    # # pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # pw_hash = "jdsofdnewofin"
    # print(pw_hash)

    # data = {
    #     'first_name': request.form['first_name'],
    #     'last_name': request.form['last_name'],
    #     'email': request.form['email'],
    #     'pw_hash': pw_hash,
    #     'updated_at': datetime.now()
    #     }
    
    # 333333 query = "INSERT INTO USERS (first_name, last_name, email, pw_hash, updated_at) VALUES (" + data['first_name'], data['last_name'], data['email'], data['pw_hash'], "2019-01-19 17:19:12"
    # 33333 query = "INSERT INTO USERS (first_name, last_name, email, pw_hash, updated_at) VALUES (%s);" % (data['first_name'], data['last_name'], data['email'], data['pw_hash'], "2019-01-19 17:19:12")

    # 33333 values = ''.join(str(x) for x in data.values())
    # columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in data.keys())
    # values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in data.values())
    # query = "INSERT INTO %s (%s) VALUES (%s);" % ("USERS", columns, values)
 
    #  data = {
    #     'first_name': request.form['first_name'],
    #     'last_name': request.form['last_name'],
    #     'email': request.form['email'],
    #     'pw_hash': pw_hash,
    #     'updated_at': datetime.now()
    #     }

    # user_id = db.query_db(query, data)
