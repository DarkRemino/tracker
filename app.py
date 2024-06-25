from flask import Flask, render_template, url_for, session, request, flash
from mdb import db_create_connection, db_submit_request
from config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY']= SECRET_KEY

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
        flash('Your package number was submitted successfully!')

        cur.close()
        conn.close()

        return render_template('track-search.html')

    return render_template('track-search.html')