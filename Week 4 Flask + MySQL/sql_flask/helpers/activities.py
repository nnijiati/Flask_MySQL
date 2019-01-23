from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
from datetime import datetime

def get_all_for_current_user(user_id):
    db = MySQLConnector(app, 'mydb_janurary')
    query = "SELECT * from activities where id=%(user_id)s;"
    data = {
    'user_id': user_id
    }
    return db.query_db(query, data)