from flaskblog import db
from flask import Flask
import os

SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

app = Flask(__name__)
app.config['SECRET_KEY']=SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI
db.init_app(app)

from flaskblog.models import User
from flaskblog.models import Post
user_1 = User(username='ali', email='ali@ali.com', iban='TR123456789012345678901234', password='password')

with app.app_context():
    db.create_all()
    db.session.add(user_1)
    db.session.commit()
    print(User.query.all())
    db.drop_all()
    db.create_all()
    print(User.query.all())
