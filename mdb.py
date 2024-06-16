# This is the configuration file for MariaDB, as well as all the functions associated with it
# All functions from here begin with the db_ prefix so it's clear what they do

import mariadb
from dotenv import load_dotenv
import os

load_dotenv()
# If you're wondering where these vars come from, check .env.example
def db_create_connection():
    conn = mariadb.connect(
        host = os.getenv('MDB_HOST'),
        user = os.getenv('MDB_USER'),
        password = os.getenv('MDB_PASSWORD'),
        database = os.getenv('MDB_SCHEMA')
    )
    return conn

def db_submit_request(tracking_number, cursor):
    cursor.execute('insert into requests(tracking_code) values(?)', (tracking_number,))