from flask import Flask
from mysqlconnection import connectToMySQL

app = Flask(__name__)

db = connectToMySQL(db="mydb_janurary")
query = "SELECT * FROM  users;"
print (db.query_db(query))