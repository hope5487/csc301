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


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    return render_template('checkout.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form['username']
        psw = request.form['password']
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
    app.run(host='0.0.0.0')
    print("abc")
