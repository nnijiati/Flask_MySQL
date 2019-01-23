from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
from datetime import datetime

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key="fdsfoenoin"

def get_all_locations():
    db = MySQLConnector(app, 'mydb_janurary')
    query = "SELECT * from Locations;"
    return db.query_db(query)
