from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))

@app.route('/')
def home():

    return 'ok'

@app.route('/add')
def add():

    user1 = User(username='user1', email='email1@gmail.com')
    user2 = User(username='user2', email='email2@gmail.com')
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    return 'ok'

@app.route('/read')
def Read():

    users = User.query.all()

    return f'{users[0].username}:{users[0].email}<br>{users[1].username}:{users[1].email}'

if __name__ == '__main__':
    app.run(debug=True)