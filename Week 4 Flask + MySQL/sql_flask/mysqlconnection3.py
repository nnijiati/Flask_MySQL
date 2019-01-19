""" import the necessary modules """
from flask_sqlalchemy import *
# import sqlalchemy
# from sqlalchemy import *
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
# from flask_mysqldb import MySQL
from sqlalchemy.sql import text


# Create a class that will give us an object that we can use to connect to a database
class MySQLConnection(object):
    # def __init__(self, db):
    #     # config = {
    #     #         'host': 'localhost',
    #     #         'database': db, # we got db as an argument
    #     #         'user': 'root',
    #     #         'password': 'root',
    #     #         'port': '3306' # change the port to match the port your SQL server is running on
    #     # }

    #     db = mysql.connector.connect(
    #     host="localhost",
    #     user="root",
    #     passwd="Nadiya88",
    #     auth_plugin='mysql_native_password'
    #     )
        # this will use the above values to generate the path to connect to your sql database
        # DATABASE_URI = "mysql://{}:{}@127.0.0.1:{}/{}".format(config['user'], config['password'], config['port'], config['database'])
        # app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
        # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        # establish the connection to database
        # self.db = mysql.connector.connect()
    # this is the method we will use to query the database
    def query_db(self, query):
        # result = self.db.session.execute(text(query), data)
        # db = mysql.connector.connect()
        db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Nadiya88",
        auth_plugin='mysql_native_password'
        )
        mycursor = db.cursor()
        result = mycursor.execute(query)
        # if query[0:6].lower() == 'select':
        #     # if the query was a select
        #     # convert the result to a list of dictionaries
        #     list_result = [dict(r) for r in result]
        #     # return the results as a list of dictionaries
        #     return list_result
        # elif query[0:6].lower() == 'insert':
        #     # if the query was an insert
    	#     # commit changes
        #     self.db.session.commit()
        #     # return the id of the row that was inserted
        #     return result.lastrowid
        # else:
        #     # if the query was an update or delete, return nothing and commit changes
        #     self.db.session.commit()
# This is the module method to be called by the user in server.py. Make sure to provide the db name!
# def connectToMySQL(app, db):
#     return MySQLConnection(app, db)

def connectToMySQL(self, db):
     return MySQLConnection(db)