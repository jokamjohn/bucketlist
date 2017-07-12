from flask import render_template, request, redirect, url_for
from app import app
from app.application import Application
from app.user import User


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
                user = User(request.form['name'], request.form['username'], request.form['password'])
                application = Application()
                if application.register_user(user):
                    return redirect(url_for('bucketlist'))
                return render_template('signup.html', error="You are already signed up, please login")
            error = 'The passwords do not match'

    return render_template('signup.html', error=error)


@app.route('/bucket/list')
def bucketlist():
    """
    This method shows the user buckets
    :return: 
    """
    return render_template('bucketlist.html')
