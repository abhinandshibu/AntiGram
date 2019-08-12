from app import app, db
from flask import render_template, redirect, url_for, make_response, request
from app.forms import LoginForm, SignupForm
import hashlib
from app.models import User
from flask_login import login_user, logout_user, login_required, current_user
import base64


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    incorrectlogin = False
    title = "Antigram"

    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        password_hash = (hashlib.sha1(password.encode())).hexdigest()

        user = User.query.filter_by(username=username).first()
        try:
            incorrectlogin = True
            if user.password_hash == password_hash:
                logout_user()
                login_user(user)
                response = make_response(redirect(url_for('access')))

                # encoding True/False to a byte then to base64
                admin = str(current_user.admin)
                admin = base64.b64encode(
                    admin.encode('utf-8'))

                response.set_cookie(
                    'userStatus', admin)
                # session.set_cookie('admin', current_user.admin)
                # return redirect(url_for('access'))
                return response
        except AttributeError:
            return render_template(
                '/entrance.html', incorrectlogin=incorrectlogin, form=form,
                title=title)
    return render_template(
        '/entrance.html', incorrectlogin=incorrectlogin, form=form,
        title=title)


@app.route('/access')
@login_required
def access():
    title = "Your Account"
    finish = False
    if current_user.id == 2:
        finish = True
    return render_template(
        '/access.html', title=title, displayNotAdmin=False, finish=finish)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/admin')
@login_required
def admin():
    admin = request.cookies.get('userStatus')
    admin = base64.b64decode(admin)
    if admin == b'True':
        userlist = [[0] * 4 for i in range(len(User.query.all()))]
        for count1 in range(1, len(User.query.all()) + 1):
            user = User.query.filter_by(id=count1).first()
            userlist[count1 - 1][0] = user.id
            userlist[count1 - 1][1] = user.username
            userlist[count1 - 1][2] = user.password_hash
            userlist[count1 - 1][3] = user.admin
        listlength = len(userlist)
        return render_template(
            'admin.html', userlist=userlist, listlength=listlength)
    else:
        # finish to tell them if they have breached Abhinand's account
        finish = False
        if current_user.id == 2:
            finish = True
        return render_template(
            '/access.html', title="Your Account", displayNotAdmin=True,
            finish=finish)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    logout_user()
    title = "Sign Up"
    form = SignupForm()
    usernameTaken = False
    passwordMatch = True

    if form.validate_on_submit():
        username = form.username.data
        password1 = form.password1.data
        password2 = form.password2.data
        user = User.query.filter_by(username=username).scalar()
        print(user)
        if (user is not None) or (password1 != password2):
            usernameTaken = False
            passwordMatch = True
            if user is not None:
                usernameTaken = True
            if password1 != password2:
                passwordMatch = False
            return render_template(
                'signup.html', form=form, title=title,
                usernameTaken=usernameTaken, passwordMatch=passwordMatch)

        password_hash = (hashlib.sha1(password1.encode())).hexdigest()
        db.session.add(
            User(username=username, password_hash=password_hash, admin=0))
        db.session.commit()
        user = User.query.filter_by(username=username).first()
        login_user(user)

        return redirect(url_for('access'))

    return render_template(
            'signup.html', form=form, title=title,
            usernameTaken=usernameTaken, passwordMatch=passwordMatch)
