"""Csc301 Web App"""
from typing import Optional, Any

from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

select1 = 10.0
select2 = 20.0
total = 33.9
option = 0.0
tax = 3.9
dp = 0.0
dc = 0.0


class User(db.Model):
    __table_name__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Coupon(db.Model):
    __table_name__ = 'coupon'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80), unique=True)
    percent = db.Column(db.Integer)

    def __init__(self, code, percent):
        self.code = code
        self.percent = percent


@app.route('/')
@app.route('/<float:num1>%<float:num2>%<float:shipping>%<float:vat>%<float:discount_percent>%'
           '<float:result>%<float:discount_total>')
def home(num1=10.0, num2=20.0, result=33.9, shipping=0.0, vat=3.9, discount_percent=dp, discount_total=dc):
    print("home dc: " + str(discount_total))
    return render_template('index.html', num1=num1, num2=num2, result=result,
                           shipping=shipping, vat=vat, discount_percent=discount_percent, discount_total=discount_total)


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    global select1, select2, total, option, tax, dc, dp
    if request.method == 'POST':
        select1 = float(request.form.get('select1'))
        select2 = float(request.form.get('select2'))
        option = float(request.form['radio-shipping'])
    dt = (select1 + select2) * 0.01 * dp
    dc = round(dt, 2)
    print(dc)
    price_before_tax = select1 + select2 + option - dt
    tax = round(price_before_tax * 0.13, 2)
    total = round(price_before_tax * 1.13, 2)
    return redirect(url_for('home', num1=select1, num2=select2, result=total,
                            shipping=option, vat=tax, discount_percent=dp, discount_total=dc))


@app.route('/discount', methods=['POST'])
def discount():
    global dp
    if request.method == 'POST':
        discount_code = request.form['discount_code']
        coupon = Coupon.query.filter_by(code=discount_code).first()
        if coupon is not None:
            dp = int(coupon.percent)
            return redirect(url_for('calculate'))
    return redirect(url_for('home'))


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
