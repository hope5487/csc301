"""Csc301 Web App"""
from typing import Optional, Any

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


@app.route('/')
@app.route('/<float:num1>%<float:num2>%<float:result>')
def home(num1=10.0, num2=20.0, result=33.9):
    return render_template('index.html', num1=num1, num2=num2, result=result)


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        select1 = float(request.form.get('select1'))
        print(select1)
        select2 = float(request.form.get('select2'))
        print(select2)
        option = float(request.form['shipping'])
        result = round((select1 + select2 + option) * 1.13, 2)
    else:
        return None
    return redirect(url_for('home', num1=select1, num2=select2, result=result))


@app.route('/checkout', methods=['POST'])
def checkout():
    return render_template('checkout.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form['username']
    password = request.form['password']
    data = User.query.filter_by(username=username, password=password).first()
    if data is not None:
        session['logged_in'] = True
        return redirect(url_for('home'))
    else:
        session['logged_in'] = False
    return redirect(url_for('login'))


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
            return redirect(url_for('login'))
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
