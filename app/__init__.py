from flask import Flask
import pymysql

app = Flask(__name__)

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='hotel_campus_db',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

from app import routes
