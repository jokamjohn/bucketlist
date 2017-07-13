from flask import render_template, request, redirect, url_for, session
from app import app
from app.application import Application
from app.models import User
from app.models import Bucket
from app.models import BucketItem

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
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    if request.method == 'POST':
        name = request.form['name']
        if user.create_bucket(Bucket(application.generate_random_key(), name)):
            return redirect(url_for('bucketlist'))
        error = "Could not create the Bucket, it already exists"
    return render_template('bucketlist.html', error=error, buckets=user.get_buckets())


@app.route('/edit/bucket/<bucket_id>', methods=['GET', 'POST'])
def editbucket(bucket_id):
    """
    This route enables a user to edit their buckets
    :param bucket_id: 
    :return: 
    """
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    bucket = user.get_bucket(bucket_id)
    if not bucket:
        return redirect(url_for('bucketlist'))
    if request.method == 'POST':
        if request.form['name']:
            if user.update_bucket(bucket_id, request.form['name']):
                return redirect(url_for('bucketlist'))
        error = "Please provide the bucket name"
    return render_template('editbucket.html', error=error, bucket=bucket)


@app.route('/delete/bucket/<bucket_id>', methods=['GET', 'POST'])
def deletebucket(bucket_id):
    """
    This route enables a user to delete a bucket
    :param bucket_id: 
    :return: 
    """
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    bucket = user.get_bucket(bucket_id)
    if not bucket:
        return redirect(url_for('bucketlist'))

    if request.method == 'POST':
        if user.delete_bucket(bucket_id):
            return redirect(url_for('bucketlist'))
        error = "Could not delete the Bucket"
    return render_template('deletebucket.html', error=error, bucket=bucket)


@app.route('/bucket/items/<bucket_id>', methods=['GET', 'POST'])
def bucketitems(bucket_id):
    """
    Route to show and create bucket items.
    :param bucket_id: 
    :return: 
    """
    error = None
    user = application.get_user(session['username'])
    if not user:
        return redirect(url_for('login'))
    bucket = user.get_bucket(bucket_id)
    if not bucket:
        return redirect(url_for('bucketlist'))

    if request.method == 'POST':
        if request.form['name']:
            if bucket.create_item(
                    BucketItem(application.generate_random_key(), request.form['name'], request.form['description'],
                               request.form['deadline'])):
                return redirect(url_for('bucketitems', bucket_id=bucket.id))
        error = "Item cannot be created"
    return render_template('bucketlistitem.html', error=error, bucket=bucket)


