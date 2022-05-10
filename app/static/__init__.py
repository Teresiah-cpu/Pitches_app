from crypt import methods
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from app import db

app = Flask(__name__)

app.config['SECRET_KEY'] = 'teresiah1githua23'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///site.db'

db = SQLAlchemy(app)




from app import routes