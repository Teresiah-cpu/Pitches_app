
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm, LoginForm
# from models import User, Pitch


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
# app.config['SECRET_KEY'] = 'teresiah1githua123'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)



pitches = [
    {
        'author': 'Teresiah',
        'title': 'Entertainment pitches',
        'content': 'Always be happy',
        'date_posted': 'May 2, 2022'
    },
    {
        'author': 'Bobo',
        'title': 'Motivational pitches',
        'content': 'Be yourself',
        'date_posted': 'April 11, 2022'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', pitches=pitches)


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


if __name__ == '__main__':
    app.run(debug=True)