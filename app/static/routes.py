from flask import render_template,flash,redirect, url_for
from app import app
from app.form import RegistrationForm, LoginForm
from app.models import User, Post


pitches = [
    {
            'author': 'Teresiah',
            'title':  'Pitch1',
            'content': 'My first pitch',
            'date_created': 'May 8, 2022'
        },
        {
            'author': 'Wambui',
            'title':  'Pitch2',
            'content': 'My second pitch',
            'date_created': 'May 9, 2022'
        
        }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',pitches=pitches)

# @app.route("/register")
# def registering():
#     return render_template('register.html')




# @app.route("/login")
# def loginn():
#     return render_template('login.html')
# creating register and login forms routes

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)