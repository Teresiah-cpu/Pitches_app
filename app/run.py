from flask import Flask, render_template
app = Flask(__name__)

pitches = [
    {
            'author': 'Teresiah',
            'title':  'Pitch',
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

@app.route("/register")
def register():
    return render_template('register.html')



@app.route("/login")
def login():
    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)