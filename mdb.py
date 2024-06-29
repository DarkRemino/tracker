# This is the configuration file for MariaDB, as well as all the functions associated with it
# All functions from here begin with the db_ prefix, so it's clear what they do

import mariadb
from dotenv import load_dotenv
import hashlib as hl
from config import MDB_HOST, MDB_USER, MDB_PASSWORD, MDB_SCHEMA  # This is supposed to error out, read config-example.py

load_dotenv()


# If you're wondering where these vars come from, check .env.example
def db_create_connection():
    conn = mariadb.connect(
        host=MDB_HOST,
        user=MDB_USER,
        password=MDB_PASSWORD,
        database=MDB_SCHEMA
    )
    return conn


def db_submit_request(tracking_number):
    with db_create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('insert into requests(tracking_code) values (?)', (tracking_number,))
            conn.commit()


def db_register_user(email, password, newsletter):
    with db_create_connection() as conn:
        with conn.cursor() as cursor:

            hashed_password = hl.sha256(password.encode('utf-8')).hexdigest()

            cursor.execute('select id from users where email=?', (email,))
            user_check = cursor.fetchone()

            if user_check != '':
                return 0 # This email is already registered with us? Have you forgotten your password?
            
            cursor.execute('insert into users(email, password, newsletter) values(?,?,?)', (email, hashed_password, newsletter))
            conn.commit()
            return 1
        

def db_login_user(email, password):
    with db_create_connection() as conn:
        with conn.cursor() as cursor:
            
            hashed_password = hl.sha256(password.enconde('utf-8')).hexdigest()

            cursor.execute('select id from users where email=? and password=?', (email, hashed_password))
            user_check = cursor.fetchone()

            if user_check == '':
                return 0 # This combination of email and password doesn't exist!
            
            return user_check[0][0] # The user's id (the result from the cursor is always a list of tuples)


def db_delete_user(email):
    with db_create_connection() as conn:
        with conn.cursor() as cursor:

            # Check if said user actually exists
            cursor.execute('select id from users where email=?', (email,))
            user_check = cursor.fetchone()

            if user_check == '':
                return 0 # We couldn't find a user with the email specified!

            cursor.execute('delete from users where email=?', (email,))
            conn.commit()
            return 1            


def db_change_user_password(email, old_password, new_password):
    with db_create_connection() as conn:
        with conn.cursor() as cursor:

            old_password_hash = hl.sha256(old_password.encode('utf-8')).hexdigest()
            new_password_hash = hl.sha256(new_password.encode('utf-8')).hexdigest()

            cursor.execute('select id from users where email=? and password=?', (email, old_password_hash))
            user_check = cursor.fetchone()

            if user_check == '':
                return 0 # Sorry, you didn't match the old password for this account! Please try again!
            
            cursor.execute('update users set password=? where email=?', (new_password_hash, email))
            conn.commit()
            return 1