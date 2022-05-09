
from flask import Flask, render_template
from form import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'teresiah1githua23'

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
def home():
    return render_template('home.html', pitches=pitches)

# @app.route("/register")
# def registering():
#     return render_template('register.html')




@app.route("/login")
def loginn():
    return render_template('login.html')
# creating register and login forms routes

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)