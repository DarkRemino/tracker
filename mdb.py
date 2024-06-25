# This is the configuration file for MariaDB, as well as all the functions associated with it
# All functions from here begin with the db_ prefix so it's clear what they do

import mariadb
from dotenv import load_dotenv
from config import MDB_HOST, MDB_USER, MDB_PASSWORD, MDB_SCHEMA

load_dotenv()
# If you're wondering where these vars come from, check .env.example
def db_create_connection():
    conn = mariadb.connect(
        host = MDB_HOST,
        user = MDB_USER,
        password = MDB_PASSWORD,
        database = MDB_SCHEMA
    )
    return conn

def db_submit_request(tracking_number, cursor):
    cursor.execute('insert into requests(tracking_code) values(?)', (tracking_number,))