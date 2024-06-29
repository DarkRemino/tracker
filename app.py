from flask import Flask, render_template, url_for, session, request, flash, redirect
from mdb import db_submit_request, db_register_user, db_login_user
from forms import RegistrationForm, LoginForm
from config import SECRET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/track', methods=['GET', 'POST'])
def landing():

    if request.method == 'POST':

        tracking_number = request.form['tracking_number']

        db_submit_request(tracking_number)
        flash('Your package number was submitted successfully!')

        return render_template('track-search.html')

    return render_template('track-search.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    register_form = RegistrationForm()

    if register_form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']
        newsletter = request.form['newsletter']

        registration_attempt = db_register_user(email, password, newsletter)

        if registration_attempt == 0:
            flash('This email has already been registered!')
            return redirect(url_for('login'))
        else:
            flash("You've successfully registered, you can now log in")
            return redirect(url_for('login'))

    return render_template('register.html', register_form=register_form)


@app.route('/login', methods=['GET', 'POST'])
def login():

    login_form = LoginForm()

    if login_form.validate_on_submit():
        email = request.form['email']
        password = request.form['password']

        login_attempt = db_login_user(email, password)

        if login_attempt == 0:
            flash('The email or password you entered is invalid!')
            return redirect(url_for('login'))
        else:
            flash("Welcome, " + email)
            return redirect(url_for('landing'))

    return render_template('login.html')
