# This is the configuration file for MariaDB, as well as all the functions associated with it
# All functions from here begin with the db_ prefix, so it's clear what they do

import pymysql
import hashlib as hl
from config import MDB_HOST, MDB_USER, MDB_PASSWORD, MDB_SCHEMA  # This is supposed to error out, read config-example.py

# If you're wondering where these vars come from, check .env.example
def db_create_connection():
    conn = pymysql.connect(
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

            if user_check is not None:
                return 0  # This email is already registered with us? Have you forgotten your password?

            cursor.execute('insert into users(email, password, newsletter) values(?,?,?)', (email, hashed_password, newsletter))
            conn.commit()
            return 1


def db_login_user(email, password):
    with db_create_connection() as conn:
        with conn.cursor() as cursor:
            hashed_password = hl.sha256(password.encode('utf-8')).hexdigest()

            cursor.execute('select id from users where email=? and password=?', (email, hashed_password))
            user_check = cursor.fetchone()

            if user_check is None:
                return 0  # This combination of email and password doesn't exist!

            return user_check[0][0]  # The user's id (the result from the cursor is always a list of tuples)


def db_delete_user(email):
    with db_create_connection() as conn:
        with conn.cursor() as cursor:
            # Check if said user actually exists
            cursor.execute('select id from users where email=?', (email,))
            user_check = cursor.fetchone()

            if user_check is None:
                return 0  # We couldn't find a user with the email specified!

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

            if user_check is None:
                return 0  # Sorry, you didn't match the old password for this account! Please try again!

            cursor.execute('update users set password=? where email=?', (new_password_hash, email))
            conn.commit()
            return 1


# As this function is supposed to work even for emails that don't have an account associated with them,
# it has an additional table only for emails (which I'll implement later)
def db_subscribe_to_newsletter(email):
    with db_create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('select id from email where email=?', (email,))
            user_check = cursor.fetchone()

            if user_check is None:
                cursor.execute('insert into email_only_newsletter(email) values(?)', (email,))
                return 0  # Despite not having an account, you can still receive news via email from us!

            cursor.execute('update users set newsletter=1 where email=?', (email,))
            return 1  # You are now successfully subscribed ot our newsletter!


def db_unsubscribe_from_newsletter(email):
    with db_create_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute('select id from email_only_newsletter where email=?', (email,))
            user_check = cursor.fetchone()
            cursor.execute('select id from users where email=?', (email,))
            user_check_2 = cursor.fetchone()

            if user_check is not None:
                cursor.execute('delete from email_only_newsletter where email=?', (email,))
                conn.commit()
                return 1
            if user_check_2 != '':
                cursor.execute('update users set newsletter=0 where email=?', (email,))
                conn.commit()
                return 1

            return 0  # We couldn't find this email in our system, so you've already been unsubscribed!
