"""Csc301 Web App"""

from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __table_name__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Product(db.Model):
    __table_name__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    price = db.Column(db.Float(80))
    quantity = db.Column(db.Float(80))

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.quantity = 0


class Coupon(db.Model):
    __table_name__ = 'coupon'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), unique=True)
    percent = db.Column(db.Integer)

    def __init__(self, code, percent):
        self.code = code
        self.percent = percent


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    return render_template('checkout.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    verify(username, password)


def verify(name, psw):
    data = User.query.filter_by(username=name, password=psw).first()
    if data is not None:
        session['logged_in'] = True
    else:
        session['logged_in'] = False
    return redirect(url_for('home', num=None))


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        """Check username is available"""
        data = User.query.filter_by(username=username).first()
        if data is None:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            return render_template('login.html')
        return render_template('register2.html')
    return render_template('register1.html')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('home', num=None))


if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.run()
