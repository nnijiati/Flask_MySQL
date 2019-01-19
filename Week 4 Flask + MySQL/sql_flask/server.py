# from flask import Flask, render_template, redirect, session, request, flash
# from flask_bcrypt import Bcrypt
# from mysqlconnection import connectToMySQL
# import re

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# app = Flask(__name__)
# bcrypt = Bcrypt(app)
# app.secret_key="fdsfoenoin"

# @app.route('/')
# def index():
#     if 'user_id' not in session:
#         return redirect('/users/new')
#     # return render_template("index.html")

# @app.route('/dashboard')
# def go_to_dashboard():
#         return render_template("dashboard.html")

# @app.route('/users/new')
# def new_user():
#     return render_template("new_user.html")

# @app.route('/users/create', methods=['POST'])
# def create():
#     errors = []
#     if len(request.form['first_name']) < 2:
#         errors.append('First name must be at least 2 characters long')

#     if len(request.form['last_name']) < 2:
#         errors.append('Last name must be at least 2 characters long')

#     if len(request.form['password']) < 8:
#         errors.append('Password must be at least 8 characters long')

#     if request.form['password'] != request.form['confirm']:
#         errors.append('Passwords do not match')

#     if not EMAIL_REGEX.match(request.form['email']):
#         errors.append("Email must be valid")
    
#     if errors:
#         for error in errors:
#             flash(error)
#         return redirect('/users/new')
#     pw_hash = bcrypt.generate_password_hash(request.form['password'])
#     print(pw_hash)

#     print ("YAYY LOGGED IN")
#     return redirect('/dashboard')

#     db = connectToMySQL(app, "mydb_janurary")
#     query1 = 'SELECT * FROM  users;'
#     query = 'INSERT INTO USERS (first_name) VALUES (%(first_name)s);'

#     # , last_name, email, pw_hash, created_at
#     # , %(last_name)s, %(email)s, %(pw_hash)s, NOW())

#     data = {
#         'first_name': request.form['first_name']
#         # 'last_name': request.form['last_name'],
#         # 'email': request.form['email'],
#         # 'pw_hash': pw_hash,
#     }

#     existing_user_data = db.query_db(query1)
#     user_id = db.query_db(query, data)
#     session['user_id'] = user_id
#     print("**************")
#     print(existing_user_data)

# @app.route('/login', methods=['POST'])
# def login():
#     pass

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
# connect and store the connection in "mysql"; note that you pass the database name to the function
mysql = MySQLConnector(app, 'mydb')
# an example of running a query
print (mysql.query_db("SELECT * FROM users"))
app.run(debug=True)
