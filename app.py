from flask import Flask, render_template, url_for, session, request
from mdb import db_create_connection, db_submit_request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/track', methods=['GET', 'POST'])
def landing():
    
    conn = db_create_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        tracking_number = request.form.get("tracking_number")
        db_submit_request(tracking_number, cur)

        cur.close()
        conn.close()
        
    return render_template('track-search.html')