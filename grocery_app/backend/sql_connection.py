import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv(override=True)

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
NAME = os.getenv("DB_NAME")

__cnx = None

def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user=USER, password=PASSWORD,
                                    host=HOST,
                                    database=NAME)
        
    return __cnx