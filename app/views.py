from flask import render_template, request, redirect, url_for, session
from app import app
from app.application import Application
from app.models import User
from app.models import Bucket

application = Application()


@app.route('/')
@app.route('/home')
def index():
    """
    This method returns the home page of the application
    :return: 
    """
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    This method shows the user the sign up page. It also signs up a user
    if all the required attributes are present and then redirects the
    user to their bucket list
    :return: 
    """
    error = None
    if request.method == 'POST':
        if request.form['name'] and request.form['username'] and request.form['password'] \
                and request.form['password-confirmation']:

            if request.form['password'] == request.form['password-confirmation']:
                user = User(request.form['username'], request.form['password'], request.form['name'])
                if application.register_user(user):
                    return redirect(url_for('login'))
                return render_template('signup.html', error="You are already signed up, please login")
            error = 'The passwords do not match'

    return render_template('signup.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    This method logins in an already existing user if their username and password
    match those already stored.
    It also shows errors to the user if their password is wrong or they do not 
    already have an account.
    :return: 
    """
    error = None
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            if application.does_user_exist(request.form['username']):
                if application.login_user(request.form['username'], request.form['password']):
                    session['username'] = request.form['username']
                    return redirect(url_for('bucketlist'))
                return render_template('login.html', error="Incorrect password")
            return render_template('login.html', error="No account found, please sign up first")
        error = "Invalid credentials, try again"
    return render_template('login.html', error=error)


@app.route('/bucket/list', methods=['GET', 'POST'])
def bucketlist():
    """
    This method shows the user buckets.
    When its a Post request a bucket is created
    and attached to the user. Then redirected back 
    :return: 
    """
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        user.create_bucket(Bucket(application.generate_random_key(), name))
        return redirect(url_for('bucketlist'))
    return render_template('bucketlist.html', buckets=user.get_buckets())
